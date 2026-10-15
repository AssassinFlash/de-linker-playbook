---
wayfinder: task
status: closed
assignee: claude-code activation-list-intake 2026-10-15
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

## 审稿交接（「操作者审稿」关票时写入，2026-10-15）

- 本票只做到第 2 阶段调研，调研是内部材料，不需要逐份审稿（操作者想看随时可看）。名单公司进入外展以后，外展信按 `docs/feedback-rules.md` 第 10 节审稿，有 `operator_ok` 才发。
- 获客台账「审批与过期」表现在多一列 `operator_ok`（在 evidence_gate 后面）；内部材料填「—」。

## Resolution（2026-10-15）

- **名单进了 vault**：操作者给的原表复制到 vault `lead/00-system/activation-list/original/`，与源文件 SHA-1 一致，没有改动。转出的 `activation-list.csv` 在同一目录，UTF-8 带 BOM，一位联系人一行。
  - 共 7966 行（原表另有 1001 个空行，不转），7904 家公司（`list_id` L-0001 起）。
  - 逐格对照原表：0 处不一致（490 格只去掉了首尾空格）。重跑转格式输出完全相同，同一家的编号不变。
- **列定义**：`schemas/activation-list.schema.json`，公开，没有数据。脚本 `uv run scripts/activation_list.py convert | progress | show --id`。原表出现没定义的列时，脚本报错停下，不会静默丢列。
- **只加入口**：
  - `lead-company-research` 加名单模式（`references/list-mode.md`），是同一 skill 的第三种交付物，一家一份 `02-companies/activation/<list_id>.md`，结论写 `list_verdict`（可接触 / 暂不接触 / 查无此公司）。
  - `lead-contact-discovery` 步骤 1：名单公司的联系人以名单为准，硬依赖是这家的调研已过闸且结论为可接触。
  - 依赖图加 `lead-company-research/list -> []`、`lead-contact-discovery/list -> [lead-company-research/list]`，加登记行和审查清单。
  - `lead-generation`：phase 2 有名单时先从名单开始，名单调研不挡 phase 推进；运营「只剩记账时」第 2 条接着调研下一家。
  - 获客台账加「激活名单」节。
  - 方法和闸门都没改。
- **走了一家**：`L-0002`（priority 1，`progress` 排在第一）。
  - 名单模式第 2 阶段：抓了 14 页官网、1 次搜索、4 个外部页。
  - 数据验证五项、六维审查 93 分（ICP 还没有，Market Relevance 一项 CONCERN）、证据闸 6 条全过，写成 `approved`，`evidence_gate: 2026-10-15`，结论 `可接触`。
  - 台账：已调研 1 / 共 7904。
- `uv run evals/validate_project.py`：All checks passed（81 skills）。
  - 新增 2 条 warning，都是「support file 找不到 `scripts/activation_list.py`」：检查器按 skill 目录解析仓库根路径，`scripts/next_step.py` 早就有同样的 warning，是检查器的老问题，不是缺文件。
