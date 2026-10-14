---
wayfinder: task
status: open
assignee:
step: 7
blocked_by: [lead-loop-orchestrator, mailbox-pullback, activation-list-intake, l3-pullback]
---

# 获客线闭环验收

## Question

（HITL）用真实动作走一遍获客线：从激活名单里一家已调研的公司出发 → 产出外展信 → 操作者手动从 chester@ 发出 → 口述 → AI 在已发送里查证并写执行登记 → 送达 / 回复回流底表与看板 → 操作者说「下一步获客」→ AI 引用这条数据给出一个动作（有回复 / 无回复 / 退信各自合理）。

- 失败的环节当轮修，修不了的切新票并在本图登记。
- 证据存 vault；公开仓库只记「通过 / 不通过 + 环节」。

## 完成标准

- 一封真实发信能沿链追到底表、看板与 AI 下一步，且下一步可回溯到规则。
