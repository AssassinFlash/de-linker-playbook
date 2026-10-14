---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
blocked_by: []
---

# 成熟的反馈分级做法

## Question

成熟的 SEO 与 B2B 外展项目，在冷启动（新站或重构后、零历史数据）阶段用哪些先行指标判断「在正轨」，以及「看到什么数据就做什么」的决策规则？

- SEO：收录率、展示、平均排名、CTR 等在新站上的典型时间线与阈值（优先 Google 官方文档与有数据支撑的行业研究）。
- B2B 冷邮件/外展：送达、回复率、正向回复率的行业基准与诊断规则（德国/DACH 若有单独数据更好）。
- 询盘（北极星）上游的漏斗指标与归因做法（小样本下如何不被噪声误导）。
- 映射到本仓库的 L0–L3（见 `CONTEXT.md`）：每级建议指标、记录粒度、触发动作的规则。

产出：`wayfinder/feasibility/research/feedback-ladder-practice.md`，每条事实带来源 URL。

## 派工记录

Grok Build 桥接会话 `8302da34-c8fc-4019-a149-143c4ef747e9`（2026-10-14 派出；`grok_status`/`grok_events` 可查）。产出：`wayfinder/feasibility/research/feedback-ladder-practice.md`。

## Resolution

冷启动「在正轨」只看两件事：重要 URL 是否被 Google 处理（收录）、信是否送达；排名进前十与询盘数都不是这阶段的合格线（Google 官方：多数站点新页至少数日、通常 3 天以上，重抓数天到数周，不保证收录；Ahrefs：随机 URL 一年内进前十仅 1.74%）。外展无通用回复率合格线（Belkins 0.45% vs Instantly 3.43%，分母不同）；100 封 0 回复是常见结果，询盘个位数时只记账不决策。**德国 UWG §7：无事先明示同意的电子邮件广告即构成骚扰**，DACH 回复率未查到。

全文：[`research/feedback-ladder-practice.md`](../research/feedback-ladder-practice.md)。主模型抽查（2026-10-14）：Google 收录时间引文出自 Search Central 现行页面。
