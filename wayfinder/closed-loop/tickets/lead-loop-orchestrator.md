---
wayfinder: task
status: open
assignee:
step: 3
blocked_by: [marketing-loop-orchestrator, execution-log-flow]
---

# 获客编排改循环

## Question

（AFK）按「营销编排改循环」同一形态重写 `skills/lead-generation`：冷启动阶段（phase 0–10）走完转运营循环，「下一步」读底表（执行登记里的发信、邮件反馈、询盘）按规则挑动作；`references/orchestration-protocol.md` 的「用户审批」闸改为证据闸 + 反馈闸（审计 #8），保留 `approved` → `stale` 的下游过期传播（可留用）。

- 复用营销侧的公共读表部分，不另写一套。
- 发信是操作者手动：外展阶段产出文案后，提示操作者发出并走「执行登记流程」。
- 邮件反馈数据由「邮箱 IMAP 回流」提供；本票不等它——底表列已定，规则照写，验收时有无数据都要能给出合理下一步（无数据 → 说明在等什么）。

- 台账（「台账拆两线」关票时写入，2026-10-14）：营销 `state/marketing-status.md`、获客 `state/lead-status.md`；旧的 `state/status.md` 已删除。两张共用键：YAML `phase`、`phase_name`、`next`、`method_skill`、`output_dir`、`product_context`（值 `docs/fact-sources.md`，`evals/validate_project.py` 会检查），同样的键再列一遍在「当前」表里，另有「阶段」「已完成」「回写」各节。获客台账另有「审批与过期」表（交付物、方法 skill、status、review_date、review_score、stale_reason、stale_date；frontmatter 为准，本表是索引）和「豁免（user_waiver）」表（日期、方法 skill、跳过的硬依赖、用户原话）。营销台账没有这两张表（只拆不改）。获客的回写规则写在台账「回写」节与 `references/orchestration-protocol.md` 步骤 7：每写一份交付物，就改「审批与过期」表里它那一行和被标 `stale` 的下游各行。用户审批闸改成证据闸 + 反馈闸后，「审批与过期」表的 status 语义要一并改掉（或换列），别留两套。

## 完成标准

- 获客台账上跑一次「下一步」：输出引用底表数据或明确说明缺哪类数据；不读写营销台账。

## 规则交接（「反馈分级规则定稿」关票时写入，2026-10-15）

- 规则正典：`docs/feedback-rules.md`。编排里不要另抄一份规则，只引用它的节号和规则编号（W-xx、M-xx、Q-xx、E-xx）。
- 「下一步」的输出格式见第 11 节；冷启动阶段和反馈怎么排（P1、P2 先做，P3–P5 让位给阶段工作）见第 7 节；证据闸清单见第 9 节，写进编排步骤。
- 每天早上会自动算一次「下一步」并发出去（第 12 节，「每日提醒」票）。所以规则匹配那一部分要做成脚本：不进对话，直接在命令行输出第 11 节格式的文字，「每日提醒」票直接调用。会话里说「下一步」时，跑同一个脚本，再由 AI 过证据闸、展开讲。
- AGENTS.md 和编排 skill 里要加一处指向 `docs/feedback-rules.md` 的指针。

## 编排交接（「营销编排改循环」关票时写入，2026-10-15）

- **公共读表部分已做好**：`scripts/next_step.py`，规则文件第 1 节有用法。邮件规则 M-01–M-15、询盘 Q-01–Q-05、执行登记 E-01–E-03 已在脚本里，获客线直接用 `--format json` 的 `actions`，不另写。
- **只要获客的动作**：
  - 按 `rule` 前缀 M、Q 筛，或按 `objects` 里的登记编号去执行登记看「线」= 获客。
  - 现在脚本不分线。要按线过滤，就在脚本里加 `--line 营销|获客`，不要在 skill 里再算一遍。
- **照营销的形态写**（`skills/marketing-orchestrator/SKILL.md`）：7 步、两种模式、「运营里只剩记账时」怎么挑新工作。
- 获客台账要加同样四个键：`mode`、`feedback_read_at`、`current_action`、`current_action_log`。`evals/validate_project.py` 的 `validate_loop` 目前只查营销台账，本票把获客台账也加进去。
- **`approved` 的含义**：营销侧已改成「已过证据闸」（AI 自查后写 `status: approved` + `evidence_gate: <日期>`）。获客「审批与过期」表的 status 要用同一个意思，或者换列，别留两套。`approved` → `stale` 的下游过期传播可以保留。
- **登记**：
  - 操作者说「发了」，AI 查证后登记。
  - 「执行登记流程」定稿前，先记进台账「待补登」表（营销台账已有这张表，获客台账照加）。
