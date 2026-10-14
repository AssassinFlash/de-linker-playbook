---
wayfinder: task
status: closed
assignee: claude-code-fact-source-entry 2026-10-14
step: 0
blocked_by: []
---

# 事实源入口：三方映射替换 New

## Question

（AFK）建立唯一的事实源入口，让「指路不复制」重新成立：所有 skill 与台账只指向这一个入口，入口再指向三方（竞品调研、线上站点、新站仓库）。

要做：

1. 写入口文件（位置自定，建议 `docs/` 或 `state/` 下一份，公开仓库，只写路径与角色名）。内容：三个源各在哪（vault `deliverables/marketing/00-research/competitor-study-2026-10-01/`、`deliverables/marketing/00-research/industry-research-2026-09-20/`（29–31 号写旧站，可能过期）、`https://de-linker.com/`、`~/Documents/de-linker` 里先读哪几份：`AGENTS.md`、`docs/specs/`、数据目录）；**什么问题查哪个源**；**冲突时谁为准**（线上站点 = 对外现状；新站仓库 = 规格与业主裁定，产品参数以其托管数据手册为准；竞品调研 = 市场与对手，不作本公司事实）；查不到 → 〔未证实〕→ 按没有处理。不写「问老板」。
2. 改指针（只改本票负责的文件，见下）：`CONTEXT.md`（「指路不复制」「去不锈钢化」里例子来源、「交付物」里「不接外部 vault」已过时——现为私有 vault 软链、「相对路径」）、`AGENTS.md`「产品上下文」节、`README.md`、`docs/getting-started.md`、`state/status.md` 的 `product_context`、两个编排 skill 及其 references（`skills/marketing-orchestrator/**`、`skills/lead-generation/**`）。
3. 其余 99 个 skill 文件**不在本票改**——留给「101 个 skill 改指新事实源」，以免两票并行改同一文件。

## 完成标准

- `grep -rn "Documents/New" CONTEXT.md AGENTS.md README.md docs state skills/marketing-orchestrator skills/lead-generation` 为 0。
- 入口文件能回答：「某产品参数从哪查」「对外怎么说从哪查」「竞品某事实从哪查」「冲突取哪个」。
- 不打开 `~/Documents/New` 的任何文件。

## 交接

- 「101 个 skill 改指新事实源」要用到的入口路径与引用写法（skill 里怎么写这一句指针），关票时写进那张票正文。
- 「台账拆两线」会改两个编排 skill 与 `state/status.md`；本票先关，它再动。

## Resolution

（2026-10-14）入口文件：`docs/fact-sources.md`。写了三个源各在哪、先读什么，「什么问题查哪个源」表，「冲突时谁为准」五条，读的规矩，以及 skill 里那一句指针的写法。规则：产品参数以托管数据手册为准，对外现状以线上站点为准，规格、裁定、用词、承诺以新站仓库为准（`AGENTS.md` §2 新裁定覆盖旧的），竞品调研不作本公司事实，查不到标〔未证实〕。台账键 `product_context` 保留，值改为 `docs/fact-sources.md`。

改的文件：`CONTEXT.md`（指路不复制、交付物（改为私有 vault 软链）、去不锈钢化、相对路径）、`AGENTS.md`（「产品上下文」节改为「事实源」，`docs/` 说明）、`README.md`、`docs/getting-started.md`、`state/status.md`（`product_context` 与 `next`）、`skills/marketing-orchestrator/SKILL.md`、`skills/marketing-orchestrator/references/dependency-graph.md`（含 JSON `global_gates.product_context.default`）、`skills/lead-generation/SKILL.md`、`skills/lead-generation/references/orchestration-protocol.md`、`skills/lead-generation/references/dependency-graph.md`（同上）。

核验：完成标准里的 grep 结果为 0；`evals/validate_project.py`、`evals/validate_deliverables.py` 全绿；两份依赖图里的 JSON 能解析。没打开过旧目录里的任何文件。剩余写死旧路径的是 `skills/` 下 96 个文件（不是 99 个），交给「101 个 skill 改指新事实源」。
