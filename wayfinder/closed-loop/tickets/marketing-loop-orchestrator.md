---
wayfinder: task
status: closed
assignee: claude-opus-5-5 会话 2026-10-15
step: 3
blocked_by: [ledger-split, feedback-ladder-rules, gsc-pullback, fact-source-rewire-skills]
---

# 营销编排改循环

## Question

（AFK）重写 `skills/marketing-orchestrator`（裁定 Q2、Q4）：冷启动阶段（现 phase 0–7）走完不 stop，转入运营循环；运营循环里每次「下一步」先读底表（经脚本层读，不让 agent 手抄表格），按「反馈分级规则定稿」挑一个动作，用中文说给操作者，并指向方法 skill。质量闸由用户审批改为证据闸 + 反馈闸。

- 营销台账（「台账拆两线」定的文件）加运营循环所需字段（当前模式：冷启动 / 运营；上次读反馈的时间；当前动作与其执行登记编号……由本票定）。
- 冷启动阶段里与线上真实动作挂钩的地方（上线页面、发布内容）提示操作者做完后走「执行登记流程」。
- 证据闸写进编排步骤与 `skills/marketing-playbook-standards/SKILL.md`（若存在）；`evals/` 的完成标准从「交付物非空且不是例子原文」补上证据闸检查。
- 读底表的公共部分（脚本命令、输出格式、给下一步的中文模板）放成两条线可共用的位置，「获客编排改循环」复用。

- 台账（「台账拆两线」关票时写入，2026-10-14）：营销 `state/marketing-status.md`、获客 `state/lead-status.md`；旧的 `state/status.md` 已删除。两张共用键：YAML `phase`、`phase_name`、`next`、`method_skill`、`output_dir`、`product_context`（值 `docs/fact-sources.md`，`evals/validate_project.py` 会检查），同样的键再列一遍在「当前」表里，另有「阶段」「已完成」「回写」各节。获客台账另有「审批与过期」表（交付物、方法 skill、status、review_date、review_score、stale_reason、stale_date；frontmatter 为准，本表是索引）和「豁免（user_waiver）」表（日期、方法 skill、跳过的硬依赖、用户原话）。营销台账没有这两张表（只拆不改）。循环字段只加在营销台账，并同步改「回写」节与 `skills/marketing-orchestrator/SKILL.md` 步骤 4 的完成条件。营销侧依赖检查说的「台账记录 `user_waiver`」目前在营销台账里没有落处；本票如果需要，就照获客台账的「豁免」表加一张。

## 完成标准

- 用当前真实底表跑一次「下一步」：输出引用了底表里的具体数据（哪页、哪天、什么状态）并给出一个动作；冷启动未完时仍按阶段推进，但会顺带报告反馈。
- 寒暄仍只复述台账，不改文件。

## 交接

- 公共读表部分的路径与用法，写进「获客编排改循环」正文。

## 规则交接（「反馈分级规则定稿」关票时写入，2026-10-15）

- 规则正典：`docs/feedback-rules.md`。编排里不要另抄一份规则，只引用它的节号和规则编号（W-xx、M-xx、Q-xx、E-xx）。
- 「下一步」的输出格式见第 11 节；冷启动阶段和反馈怎么排（P1、P2 先做，P3–P5 让位给阶段工作）见第 7 节；证据闸清单见第 9 节，写进编排步骤。
- 每天早上会自动算一次「下一步」并发出去（第 12 节，「每日提醒」票）。所以规则匹配那一部分要做成脚本：不进对话，直接在命令行输出第 11 节格式的文字，「每日提醒」票直接调用。会话里说「下一步」时，跑同一个脚本，再由 AI 过证据闸、展开讲。
- AGENTS.md 和编排 skill 里要加一处指向 `docs/feedback-rules.md` 的指针。

## 提前开工（2026-10-15）

- 「GSC 数据回流」还没关，只差「近 7 天展示」那部分数据（等 Google 出数）。操作者同意不等它，先开工，因为每日提醒要靠本票。原话是「现在的话可以开始做「营销编排改循环」这个」。
- 底表里现在已经有真实的网页收录数据（约 300 行），够本票验收时引用「哪页、哪天、什么状态」。网页表现那部分，等有数后规则自然会用上，不用返工。

## Resolution（2026-10-15）

- **公共读表部分**：`scripts/next_step.py`。它读底表七张表，按 `docs/feedback-rules.md` 对全部规则（网页 W、邮件 M、询盘 Q、执行登记 E），排好 P1–P5，阻断类网页规则先抓线上现状。输出两种格式：text 是规则第 11 节的中文格式，JSON 给编排判断优先级。还有两个回写命令：`mark`（AI 做完的一次性核查 W-13、W-24）和 `log-request`（GSC 请求编入索引后登记）。用法写在规则文件第 1 节。
- **编排**：`skills/marketing-orchestrator/SKILL.md` 重写成 7 步：读台账 → 分流 → 读反馈（跑脚本）→ 挑一个动作 → 做、过证据闸、按第 11 节说 → 登记做完的事 → 回写台账。
  - 两种模式：冷启动下 P1、P2 先做，其余让位给阶段工作并顺带报告；phase 7 做完转运营，不 stop。
  - 运营里只剩记账时：先补缺失或没过证据闸的交付物，再复核 `evidence_gate` 最早的那份，都没有就说在等什么。
- **质量闸**：`approved` 改成「已过证据闸」，由 AI 自查后写 `status: approved` 和 `evidence_gate: <日期>`，不需要操作者批准。改动处：
  - 依赖图（含机器可读图）、`marketing-playbook-standards`（五条硬约束，加证据闸）；
  - `marketing-positioning`、`marketing-profile` 原来的「用户确认」一步，改成证据闸；
  - `marketing-skill-eval` 的条数。
- **台账**：`state/marketing-status.md` 加 `mode`、`feedback_read_at`、`current_action`、`current_action_log`，以及「待补登」「豁免（user_waiver）」两张表，「回写」节同步改。
- **evals**：`evals/validate_project.py` 新增 `validate_loop`，查四件事：
  - 台账循环键齐全、`mode` 合法；
  - 规则文件和脚本都在；
  - 编排、共用规则、依赖图都指向它们；
  - `deliverables/marketing/` 里写了 `status: approved` 的都带 `evidence_gate` 日期。造了一份反例，确实会报错。
- **AGENTS.md**：加了一句指路，指向规则文件和脚本。
- **验收**：
  - 样例：脚本跑样例表和内置样例，结果一致，和规则第 13 节对得上。`mark`、`log-request` 在样例表上试过，样例表已重建复原。
  - 真实底表（2026-10-15 12:06）：引用了「网页收录」2026-10-15 的检查，6 个网址「被 noindex 挡住」，线上抓取都是 HTTP 200、`index, follow`；动作是在 GSC 请求编入索引一次（W-04，P3）。因为是冷启动、最高只到 P3，本轮按阶段做 phase 0，并顺带报告这件反馈。台账已回写 `feedback_read_at`、`current_action`。
  - 寒暄只复述 `mode`、`phase`、`next`，不改文件（写在步骤 2 和易错里）。
