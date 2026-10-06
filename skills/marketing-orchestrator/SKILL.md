---
name: marketing-orchestrator
description: >
  Use when starting marketing, SEO, or content work in this repo, or when the
  user asks for the next step, 下一步, 营销, 文案, 内容, or a value
  proposition. Read state/status.md first; announce the current phase, the
  next method skill, and the output path; then run that work (dispatch a
  subagent, else do it inline) and update the ledger. Use this navigator
  rather than inventing a parallel workflow. Greetings get a phase recap
  only; unrelated coding does not start a run.
---

# 营销编排（导航）

读台账、宣布阶段、执行当前工作、回写台账。方法本身在方法 skill 里。

## 步骤

1. **读台账** `state/status.md`。完成：能报出 `phase`、`next`、`method_skill`、`output_dir`、`product_context`。
2. **分流**。推进意图（下一步 / 营销 / 文案 / 内容 / 价值主张 / “Do the next step…”）→ 步骤 3。寒暄或无关问题 → 复述 `phase` 与 `next`，停。
3. **从当前 phase 做到交付物落地**，按台账「阶段」表。每完成一阶段先回写台账再继续。
   - **0** 只读 `product_context`（路径以台账为准；不把原文写入本仓库）。完成：三条陈述（买家、所卖、缺口）；`phase: 1`。
   - **1** 先读 `skills/marketing-copywriting/SKILL.md`，再按其步骤做。需要隔离时 dispatch a subagent, else do it inline。完成：`deliverables/value-proposition.md` 非空；`phase: 2`。
   - **2** 报告产物路径，停。
4. **回写台账**（步骤 3 的每个 phase 边界都做）。完成：YAML、「当前」表、「已完成」与磁盘一致；`next` 指向下一动作或 `stop`。

## 默认

- 进度只认台账。
- 产出只进台账的 `output_dir`。
- 产品事实只读，不在本仓库另存一份。

## 清单

- [ ] 已读台账并当众宣布 phase / 下一 skill / 产出路径
- [ ] 推进时按方法 skill 做完，而不是自造流程
- [ ] 交付物不是 skill 例子原文
- [ ] 台账已回写
