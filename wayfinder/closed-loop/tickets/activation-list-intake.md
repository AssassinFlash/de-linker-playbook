---
wayfinder: task
status: open
assignee:
step: 6
blocked_by: [lead-loop-orchestrator, fact-source-rewire-skills]
---

# 激活名单入口

## Question

（HITL 交名单 + AFK 改 skill）按裁定 Q7 接上激活名单：名单放私有 vault `deliverables/lead/00-system/`；获客第 2 阶段以名单公司为起点逐家调研，第 3 阶段联系人以名单为准；其余按陌生开发。

- 名单格式：列定义写进 `schemas/`（公开，无数据）；操作者把老板给的表放进 vault（agent 可帮转格式，原件不动）。名单本身绝不进公开仓库。
- 改获客台账与编排（「获客编排改循环」之后的形态）：第 2 / 3 阶段的输入多一个「名单」来源；改 `lead-company-research`、`lead-contact-discovery` 及 `lead-generation/references/dependency-graph.md` 中相关处，只加入口，不改方法。
- 「已同意」只解除发信顾虑，不提供客户认知：skill 里写明按陌生开发先调研再接触（`CONTEXT.md`「激活名单」）。

## 完成标准

- 用名单中一家公司走一次第 2 阶段：产出落 `deliverables/lead/02-companies/`，来源列齐；台账显示名单进度（已调研 n / 共 N）。

## 获客编排交接（「获客编排改循环」关票时写入，2026-10-15）

- **编排已改成循环**：`skills/lead-generation/SKILL.md` 有 7 步，冷启动 phase 0–10，之后转运营。第 2、3 阶段照旧走 `references/orchestration-protocol.md` 步骤 0–7（依赖检查 → 意图确认 → 方法 skill → 数据验证 → 六维审查 → 证据闸 → 写入与过期）。名单入口只加在「输入」，闸门不用另写。
- **`approved` 的意思**：已过证据闸，两条线同一个意思。名单公司的调研交付物要先过六维审查，再过 `docs/feedback-rules.md` 第 9 节，然后写 `status: approved` 和 `evidence_gate: <日期>`。
  - `approved_with_concerns` 已经取消，concern 记在 `review_concerns`。`evals/validate_project.py` 发现 `deliverables/lead/` 里有 `approved` 不带 `evidence_gate`，或者出现旧状态，都会报错。
  - 台账「审批与过期」表的列是：交付物、方法 skill、status、evidence_gate、review_score、stale_reason、stale_date。
- **名单进度放在获客台账**：新加一节，比如「激活名单」，写已调研 n / 共 N。只写数字和 vault 相对路径，公司名不进公开仓库。
  - `validate_loop` 查获客台账时，要求这些字样在：`待补登`、`evidence_gate`，以及四个循环键。新加的一节不要把它们弄丢。
- **公司名写法要一致**：「运营里只剩记账时」第 1 条会拿外展交付物里已过闸的收件公司，去对 `uv run scripts/execution_log.py show` 的「收件公司」列，找还没发出的。询盘归因也按公司对。所以名单、调研交付物、外展交付物、执行登记里的公司名，要用同一种写法（原文，不翻译）。
- 外展信只产文案，由操作者手动发；发完按 `skills/marketing-execution-log/SKILL.md` 登记，带 `--line 获客`。
