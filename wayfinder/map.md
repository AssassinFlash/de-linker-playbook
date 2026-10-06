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
- **试点先行（用户定）**：不做纯假设——先调研、再做最小薄片实测、走通才跑量。假设 ≠ 证据（Claude 的编排是内置设施，通用 harness 的可移植性必须实测验证）。
- **兼容目标 = 五家（用户定 2026-10-06）**：Kimi、Z Code、DeepSeek、OpenCode、Hermes。其余 harness（Claude、Codex 等）不在兼容范围，不为它们做适配层。
- **执行节奏（用户定 2026-10-06）**：每票用一个新会话/新窗口执行，不在长会话里连续走票——保护上下文质量，避免反复压缩。新会话进场先读本图，认领前沿票，干完关票。
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

- [跨 harness skill 约定与最新编写最佳实践调研](tickets/skill-conventions-research.md)：正典只要 name+description+正文（<500 行）；发现层事实标准 = `.agents/skills/<name>` 软链 + 根级 AGENTS.md（裸 skills/ 无人自动扫描）；description 是触发器（300–700 字符、触发词前置）。全文：`wayfinder/research/skill-conventions-best-practices-2026-10.md`。
- [通用 harness 编排机制调研](tickets/generic-orchestration-research.md)：「自动触发」不可移植（各家的启动注入是 per-harness 的），可移植的是**台账文件**；正典禁用 harness 专属子代理工具名（统一写 "dispatch a subagent, else do it inline"）；AGENTS.md 只放指针、状态指针置顶（Codex 32KiB 截断）；无可移植命令约定。冷启动可行性 = 试点薄片必须实测的假设。全文：`wayfinder/research/generic-orchestration-2026-10.md`。
- [试点薄片：最小骨架 + 2 skill + 多 harness 实测](tickets/pilot-slice.md)：冷启动循环 **kimi（95s）与 codex（76s）双 PASS**，claude 因本机 OAuth 过期未测成（非薄片问题）；摩擦全在 CLI 调用层而非 playbook 内容；orchestrator + 台账模式验证可行，⑨ 的裁定有实测证据了。实测记录：`wayfinder/pilot/`。
- [编排层落地形态](tickets/orchestration-workflow-form.md)：**乙为骨 + 甲为重活**——orchestrator skill + 台账自驱动（试点双 PASS 实证），多阶段重活走 wayfinder 票；命令卡片只做按需适配器。编排系 skill 改写方向随之确定。
- [抽取规格定稿](tickets/extraction-spec.md)：38+43 个 skill 的抽取规格定稿——正典只要 name+description（300–700 字符硬标准）、v3 无前缀 23 个加 `marketing-`、evals.json 不迁、交付物双树 `deliverables/marketing|lead/` 取代外部 vault、验收 10 条可跑命令 + 冒烟 S1–S5。全文：[`wayfinder/extraction-spec.md`](extraction-spec.md)。
- [仓库骨架建立](tickets/repo-skeleton.md)：全量目录补齐（schemas/templates/evals/docs 预留）、AGENTS.md 终稿（交接说明 + 兼容五家）、README.md、CONTEXT.md 词汇表 11 词条、.gitignore 审计无缺口、软链层验证通过；New 侧已加回指。

## Not yet specified

<!-- 2026-10-06 清空。原四条全部毕业：编排层形态 → 立票「编排层落地形态」；互指写法 → 并入「仓库骨架建立」；lead-gen 产出形态 → 并入「抽取规格定稿」；适配器时机 → 已由「跨 harness 调研」回答（.agents/skills 软链 + 按需生成）。 -->

## Out of scope

- 不锈钢 6 份拷贝的清理/归档（原地不动）
- 用 playbook 实际执行营销活动（本图只到 playbook 建成可用）
- `~/Documents/New` 的 PDP 文案线（另有地图管辖）
