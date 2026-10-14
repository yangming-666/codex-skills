#!/usr/bin/env python3
"""Capture and compare static Panorama ScenePanel composition contracts.

This is deliberately a risk detector, not a Panorama renderer or cascade engine.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any


SCENE_TAGS = {"DOTAScenePanel", "DOTAParticleScenePanel"}
MUTATION_PATTERNS = {
    "SetParent": re.compile(r"\.SetParent\s*\("),
    "MoveChildAfter": re.compile(r"\.MoveChildAfter\s*\("),
    "MoveChildBefore": re.compile(r"\.MoveChildBefore\s*\("),
    "DeleteAsync": re.compile(r"\.DeleteAsync\s*\("),
    "RemoveAndDeleteChildren": re.compile(r"\.RemoveAndDeleteChildren\s*\("),
    "DynamicScenePanel": re.compile(
        r"(?:DOTAScenePanel|DOTAParticleScenePanel)", re.IGNORECASE
    ),
}
RISK_PROPERTIES = {
    "blur",
    "opacity-mask",
    "overflow",
    "transform",
    "pre-transform-scale2d",
    "z-index",
    "opacity",
    "visibility",
}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_tag(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def node_key(node: ET.Element, index: int) -> str:
    return node.attrib.get("id") or f"{local_tag(node.tag)}[{index}]"


def parse_xml(paths: list[Path]) -> tuple[list[dict[str, Any]], list[str]]:
    scenes: list[dict[str, Any]] = []
    all_ids: list[str] = []

    for path in paths:
        root = ET.parse(path).getroot()

        def walk(node: ET.Element, ancestors: list[dict[str, str]]) -> None:
            tag = local_tag(node.tag)
            panel_id = node.attrib.get("id")
            if panel_id:
                all_ids.append(panel_id)

            descriptor = {
                "tag": tag,
                "id": panel_id or "",
                "class": node.attrib.get("class", ""),
            }
            if tag in SCENE_TAGS:
                scenes.append(
                    {
                        "file": str(path),
                        "key": node_key(node, len(scenes)),
                        "tag": tag,
                        "id": panel_id or "",
                        "class": node.attrib.get("class", ""),
                        "attributes": dict(sorted(node.attrib.items())),
                        "ancestors": ancestors,
                    }
                )

            next_ancestors = ancestors + [descriptor]
            for child in list(node):
                walk(child, next_ancestors)

        walk(root, [])

    duplicates = sorted(panel_id for panel_id, count in Counter(all_ids).items() if count > 1)
    return scenes, duplicates


def strip_js_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return re.sub(r"//[^\r\n]*", "", text)


def scan_js(paths: list[Path]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in paths:
        text = strip_js_comments(path.read_text(encoding="utf-8-sig", errors="replace"))
        lines = text.splitlines()
        for name, pattern in MUTATION_PATTERNS.items():
            for number, line in enumerate(lines, 1):
                if pattern.search(line):
                    findings.append(
                        {
                            "file": str(path),
                            "line": number,
                            "kind": name,
                            "text": line.strip(),
                        }
                    )
    return findings


def scene_selectors(scenes: list[dict[str, Any]]) -> set[str]:
    selectors: set[str] = set()
    for scene in scenes:
        for entry in scene["ancestors"] + [scene]:
            if entry.get("id"):
                selectors.add("#" + entry["id"])
            for class_name in entry.get("class", "").split():
                selectors.add("." + class_name)
    return selectors


def scan_css(paths: list[Path], relevant_selectors: set[str]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    block_pattern = re.compile(r"([^{}]+)\{([^{}]*)\}", re.DOTALL)
    prop_pattern = re.compile(r"(?m)^\s*([a-zA-Z0-9-]+)\s*:\s*([^;]+);")

    for path in paths:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for match in block_pattern.finditer(text):
            selector = " ".join(match.group(1).split())
            if not any(token in selector for token in relevant_selectors):
                continue
            properties = {
                name.strip(): value.strip()
                for name, value in prop_pattern.findall(match.group(2))
                if name.strip() in RISK_PROPERTIES
            }
            if properties:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    {
                        "file": str(path),
                        "line": line,
                        "selector": selector,
                        "properties": dict(sorted(properties.items())),
                    }
                )
    return findings


def build_snapshot(args: argparse.Namespace) -> dict[str, Any]:
    xml_paths = [Path(value).resolve() for value in args.xml]
    css_paths = [Path(value).resolve() for value in args.css]
    js_paths = [Path(value).resolve() for value in args.js]
    all_paths = xml_paths + css_paths + js_paths

    missing = [str(path) for path in all_paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source file(s): " + ", ".join(missing))

    scenes, duplicate_ids = parse_xml(xml_paths)
    selectors = scene_selectors(scenes)
    return {
        "schema": 1,
        "files": {str(path): file_hash(path) for path in all_paths},
        "scene_panels": scenes,
        "duplicate_ids": duplicate_ids,
        "js_risks": scan_js(js_paths),
        "css_risks": scan_css(css_paths, selectors),
    }


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)


def compare_snapshots(baseline: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    baseline_scenes = {scene["key"]: scene for scene in baseline.get("scene_panels", [])}
    current_scenes = {scene["key"]: scene for scene in current.get("scene_panels", [])}

    added = sorted(set(current_scenes) - set(baseline_scenes))
    removed = sorted(set(baseline_scenes) - set(current_scenes))
    changed = sorted(
        key
        for key in set(current_scenes) & set(baseline_scenes)
        if stable_json(current_scenes[key]) != stable_json(baseline_scenes[key])
    )

    base_js = {stable_json(item) for item in baseline.get("js_risks", [])}
    base_css = {stable_json(item) for item in baseline.get("css_risks", [])}
    new_js = [item for item in current.get("js_risks", []) if stable_json(item) not in base_js]
    new_css = [item for item in current.get("css_risks", []) if stable_json(item) not in base_css]

    return {
        "scene_panels_added": added,
        "scene_panels_removed": removed,
        "scene_panels_changed": changed,
        "new_duplicate_ids": sorted(
            set(current.get("duplicate_ids", [])) - set(baseline.get("duplicate_ids", []))
        ),
        "new_js_risks": new_js,
        "new_css_risks": new_css,
    }


def has_drift(diff: dict[str, Any]) -> bool:
    return any(bool(value) for value in diff.values())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture or compare a static Panorama ScenePanel composition contract."
    )
    parser.add_argument("--xml", action="append", default=[], help="Loaded Panorama XML source.")
    parser.add_argument("--css", action="append", default=[], help="Loaded Panorama VCSS/CSS source.")
    parser.add_argument("--js", action="append", default=[], help="Loaded Panorama JavaScript source.")
    parser.add_argument("--write-baseline", help="Write the current snapshot as JSON.")
    parser.add_argument("--baseline", help="Compare the current snapshot with this JSON baseline.")
    parser.add_argument(
        "--enforce-baseline",
        action="store_true",
        help="Exit 2 when structural drift or new risks are found.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.xml:
        print("error: at least one --xml source is required", file=sys.stderr)
        return 2

    try:
        snapshot = build_snapshot(args)
    except (FileNotFoundError, ET.ParseError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.write_baseline:
        output = Path(args.write_baseline).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(stable_json(snapshot) + "\n", encoding="utf-8")
        print(f"baseline written: {output}")

    print(
        f"scene_panels={len(snapshot['scene_panels'])} "
        f"duplicate_ids={len(snapshot['duplicate_ids'])} "
        f"js_risks={len(snapshot['js_risks'])} "
        f"css_risks={len(snapshot['css_risks'])}"
    )

    if snapshot["duplicate_ids"]:
        print("duplicate IDs: " + ", ".join(snapshot["duplicate_ids"]))

    if args.baseline:
        baseline_path = Path(args.baseline).resolve()
        try:
            baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            print(f"error: invalid baseline: {exc}", file=sys.stderr)
            return 2
        diff = compare_snapshots(baseline, snapshot)
        print(stable_json(diff))
        if args.enforce_baseline and has_drift(diff):
            return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
