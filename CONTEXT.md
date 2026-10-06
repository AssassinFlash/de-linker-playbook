# CONTEXT.md — de-linker playbook 词汇表

- **正典（canonical）**：跨 harness 可直接阅读的 skill 本体。位于 `skills/` 下与 frontmatter `name` 同名的目录里的 `SKILL.md`：只有 `name` + `description` + 纯 markdown 正文，无 harness 专属字段（如 `model`、`allowed-tools`、`mcp__*`）。工具写成能力描述，不写某家接线名。
- **适配器（adapter）**：发现层设施与 harness 专属接线。薄、按需生成、不进正典。包括 `.agents/skills/<name>` → `../../skills/<name>` 的软链，以及 slash command、`$skill`、wrapper 等。无原生扫描器时靠根 `AGENTS.md` 指路。
- **例子定位**：例子是教学支架，不是素材库。skill 内例子必须显式标注「仅供理解，禁止引用到输出」；任何交付物不得出现例子原文。
- **指路不复制**：产品事实只在 `~/Documents/New`（先读其中 `CONTEXT.md`，需要参数再读 `fact-base/`）。本仓库只指路、不拷贝，避免第二真相源。读文件时把 `~` 展开为用户主目录，不要把 `~` 当相对路径；交接他机需更新此路径。
- **台账**：进度真源，文件为 `state/status.md`。压缩后以该文件为准，不以对话记忆为准。
- **交付物**：本仓库产出，落在 `deliverables/`。不接外部 vault。
- **去不锈钢化**：A 为骨、C 为例。正文（A）通用化、不锁任何产品；例子（C）优先取自 `~/Documents/New` 的真实材料。产品事实不写进 skill。
- **兼容目标五家**：Kimi、Z Code、DeepSeek、OpenCode、Hermes。其余 harness（Claude、Codex 等）不在兼容范围，不为它们做适配。
- **无上位法**：一切既有文档都是可改的活文档，包括本仓库文件、`linker-copywriting` 与 v3 原稿；不做权威绑定，尺子可以改。
- **相对路径**：仓库内一律用相对路径指路，禁止硬编码仓外绝对路径。指向产品事实的指针用 `~/Documents/New` 这种 `~` 形式，并注明要展开。
- **当轮清账**：本轮发现的问题当轮修复，不记 backlog。
