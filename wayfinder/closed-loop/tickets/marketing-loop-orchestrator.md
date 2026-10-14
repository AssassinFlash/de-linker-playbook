---
wayfinder: task
status: open
assignee:
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
