# Codex-Skill

个人维护的 Codex 技能集合，侧重 Dota 2 开发、游戏数值工作簿、图表和界面取证。

**状态：持续维护的工作流资源。** 每个技能有独立的适用范围、工具要求和验证约定；本仓库不是 Codex 应用或完整运行环境的备份。

## 技能目录

| 技能 | 主要用途 |
|---|---|
| [analyze-excel-data-structure](skills/analyze-excel-data-structure/SKILL.md) | 游戏数值与字段关系分析、工作簿结构设计 |
| [dota2-ability](skills/dota2-ability/SKILL.md) | Dota 2 Lua / KV 技能与 modifier 开发约束 |
| [dota2-panorama](skills/dota2-panorama/SKILL.md) | Panorama 布局、交互、状态和验证 |
| [dota2-particle-playback](skills/dota2-particle-playback/SKILL.md) | 粒子资源、控制点、生命周期和预载证据 |
| [dota2-sound-lookup](skills/dota2-sound-lookup/SKILL.md) | 声音事件、依赖和播放契约核对 |
| [drawio](skills/drawio/SKILL.md) | draw.io XML 图表创建与维护 |
| [pve-replica-excel](skills/pve-replica-excel/SKILL.md) | 既有 PVE 英雄技能工作簿的证据驱动更新 |
| [screenshot](skills/screenshot/SKILL.md) | 桌面截图采集工作流 |

## 使用方式

1. 克隆本仓库到独立源码目录，不要覆盖正在使用的 Codex 配置目录。
2. 阅读目标技能的 `SKILL.md`，核对适用范围、外部工具及本机路径。
3. 仅安装所需技能目录，保留其 `references/`、`scripts/` 和 `assets/`。
4. 按客户端当前支持的方式安装，参考 [OpenAI 官方技能指南](https://learn.chatgpt.com/docs/build-skills)。项目级技能可置于项目的 `.agents/skills/` 中。
5. 使用一个小型真实任务验证触发条件和输出，缺少工具或资源时明确报告，不把检查清单本身当作通过证据。

```text
skills/<skill-name>/
  SKILL.md       使用条件与流程
  references/    按需读取的参考
  scripts/       配套工具（若有）
  assets/        模板和资源（若有）
```

## 本地适配

部分 Dota 2 工作流依赖游戏资源、解包工具或作者的目录布局。使用前调整本地路径并确认资源来源；仓库不提供商业游戏资产。根目录 `AGENTS.md` 是作者的工作约束，采用前应阅读并按自己的项目范围配置。

## 仓库边界

仅跟踪技能源码、文档和维护模板。登录凭据、会话、数据库、运行状态、缓存及系统自带技能不属于本仓库内容。历史提交可能保留旧的运行环境文件；当前树清理不等价于 Git 历史清除。

## 贡献与许可

[贡献指南](CONTRIBUTING.md) · [安全说明](SECURITY.md)

尚未选择统一的仓库级开源许可证。保留各文件已有的来源和许可声明，不把第三方技能重新许可为个人作品。
