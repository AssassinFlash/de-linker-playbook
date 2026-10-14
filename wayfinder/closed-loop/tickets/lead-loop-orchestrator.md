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

## 完成标准

- 获客台账上跑一次「下一步」：输出引用底表数据或明确说明缺哪类数据；不读写营销台账。
