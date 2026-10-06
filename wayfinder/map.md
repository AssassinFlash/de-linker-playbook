---
wayfinder: map
created: 2026-10-06
---

# 地图：de-linker playbook——v3 + lead-gen 方法层抽取为跨 harness 自包含仓库

## Destination

一个自包含的 git 仓库 `~/Documents/de-linker-playbook`：`marketing-playbook-v3` 的 38 个营销 skill 与 `lead-generation_副本` 的 43 个获客 skill，经去不锈钢化、跨 harness 通用化后迁入扁平 `skills/`（`marketing-*` / `lead-*` 前缀），附 schemas/templates/eval 与根级 AGENTS.md 指路；任何 agent harness 打开即可用。验收 = 对照 review + 主模型抽查 + 真实冒烟。

## Notes

- **本图包含执行（用户定）**：图走完了活也干完了，不只产决策。
- **执行分工（用户定）**：执行一律子代理（DeepSeek 额度）；主模型只组织、review、与用户对话，额度用在刀刃上。
- **例子的定位（用户定，最高优先级）**：例子是教学支架，不是素材库。skill 内例子必须显式标注「仅供理解，禁止引用到输出」；任何交付物不得出现例子原文。
- **无上位法（用户定）**：`linker-copywriting`、v3 原稿、任何既有标准都是可改的活文档，不做权威绑定；尺子可以改。
- **跨 harness 正典（用户定）**：SKILL.md = `name` + `description` + 纯 markdown 正文；不写 harness 专属字段（`model`/`allowed-tools`/`mcp__*`）；工具写成能力描述（如「用网页搜索查证」）。harness 专属接线（slash command、`$skill`、`.kimi` wrapper）只做薄适配器、按需生成、不进正典。动机：主模型额度随时可能耗尽，工作会交接给别的 agent，任何 harness 都必须能直接看懂这个仓库。
- **去不锈钢化 = A 为骨 C 为例**：skill 正文通用化，不锁任何产品；例子优先取自 `~/Documents/New` 的真实材料。产品事实不写进 skill（避免第二真相源）；Linker 上下文指路 `~/Documents/New`（`CONTEXT.md`、`fact-base/`），指路不复制。
- **交付物落本仓库**，不接外部 vault；一律相对路径，禁止硬编码绝对路径（不锈钢线的教训：障碍是写死的仓外绝对路径，不是 Obsidian 本身）。
- **当轮清账原则（用户既有规矩）**：本轮发现的问题当轮修复，不记 backlog。
- **lead-gen 方法论来自用户自购的付费 prompt**：自用，不对外分发。
- **抽取源头**：`~/Documents/marketing-playbook-v3`（canonical = `.claude/skills/` 38 个；root `skills/` 是 legacy，不抽）；`~/Documents/lead-generation_副本`（canonical = `skills/` 43 个；`.kimi/`/`.codex/` 适配层不抽）。

## Decisions so far

<!-- 每关闭一张票，在此加一行：标题链接 + 一句话 gist。Q1–Q10 的方向性决策见 Notes。 -->

## Not yet specified

- playbook 建成后，非 PDP 的营销工作（SEO/内容/获客）在本仓库里以什么节奏跑（orchestrator 类 skill 落地后的实际工作流）
- harness 适配器何时生成、先生成哪些（等实际要在某个 harness 里使用时再定）
- 与 `~/Documents/New` PDP 线的互相引用方式（AGENTS.md 指路的具体写法）
- lead-gen 产出的形态（原系统写 LeadGen-Vault；本仓库内的对应结构）

## Out of scope

- 不锈钢 6 份拷贝的清理/归档（原地不动）
- 用 playbook 实际执行营销活动（本图只到 playbook 建成可用）
- `~/Documents/New` 的 PDP 文案线（另有地图管辖）
