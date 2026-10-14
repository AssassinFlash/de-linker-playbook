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
