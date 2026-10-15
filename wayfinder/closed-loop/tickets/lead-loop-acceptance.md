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

## 获客编排交接（「获客编排改循环」关票时写入，2026-10-15）

- **「下一步获客」**：按 `skills/lead-generation/SKILL.md` 走。脚本是 `uv run scripts/next_step.py --line 获客`，会话里先用 `--format json`，再按第 11 节说给操作者。
  - 冷启动下，只有 P1、P2 插队（真人回复 M-01 到 M-03 是 P1；永久退信 M-05、到期的下一封 M-11 是 P2）。P3–P5 让位给阶段工作，只顺带报告。
  - 验收要看三种情况：有回复 → M-01/M-02/M-03（P1）；无回复 → M-11（到期，P2）或 M-12、M-13（P5，只记账）；退信 → M-05（P2）或 M-06（P5）。
- **基线**：2026-10-15 16:31 在真实底表上，获客线 0 条登记、0 条邮件反馈、0 条询盘。输出是「今天没有要动的」，并列出在等的三样（原文见「获客编排改循环」Resolution）。验收时这三条应该变成引用具体登记编号、事件日期的动作。
- **登记那一环**：发信后按 `skills/marketing-execution-log/SKILL.md` 登记，必须带 `--line 获客`、`--company`、`--sequence S-公司名`、`--nth`。最好再带 `--planned` 和 `--next-date`，不带的话无回复时只会落到 M-13，只记账。编号写进获客台账的 `current_action_log`。
- **台账**：每轮都要回写 `feedback_read_at`、`current_action`、`current_action_log`。验收时可以对一下，营销台账没有被改。
- **询盘**：没归因的询盘两条线都会报告。只有填了「归因登记编号」、并且指向获客登记的，才只出现在获客线。
