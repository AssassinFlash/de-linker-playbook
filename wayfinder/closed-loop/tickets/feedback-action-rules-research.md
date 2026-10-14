---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
grok_session: f1549580-0ba7-4c83-9cb6-2045da4871b0
resolved: 2026-10-14
step: 3
blocked_by: []
---

# 反馈分级行动规则调研

## Question

（派 Grok Build）对反馈分级每一级、每种信号，业内有出处的「看到这个 → 下一步做什么」是什么？这是运营循环里 AI 给出下一步的依据，必须能脱离操作者的行业判断成立。

已有底子（不重做，在其上扩展）：`wayfinder/feasibility/research/feedback-ladder-practice.md`（冷启动只看收录与送达；排名与个位数询盘只记账不决策）。

须覆盖：

1. 网页：URL Inspection 各种「未收录」状态各意味着什么、对应动作（Google Search Central 现行文档为准）；收录后多久没有展示算异常；有展示无点击、有点击无询盘时的常规动作（及其所需最少数据量，样本太小时不动作的依据）。
2. 邮件：退信（硬 / 软）、无回复、自动回复、真人回复各自的下一步；跟进次数与间隔的有出处做法；德国 B2B 语境（外展对象均已同意，合规不作阻碍）。
3. 询盘：询盘个位数时的「只记账」规则如何写成可执行条件；何时可以开始据询盘调整。
4. 冷启动 → 逐级上移：有没有有出处的阈值或时间窗；没有就写「无通用阈值」，给出业内常见做法与其局限。
5. 每条规则对应本仓库哪个方法 skill（`skills/` 下名字）可承接动作——这一列由主模型验收时核对。

产出：`wayfinder/closed-loop/research/feedback-action-rules.md`，规则表（级别 / 信号 / 条件 / 动作 / 来源 / 适用前提）。查不到标〔未证实〕。

## 完成标准

- 每级至少有可执行的条件与动作；每条带来源。主模型抽查至少两条来源原文，写进 Resolution，并向用户汇报。

## Resolution

冷启动里能立刻执行的下一步只有三类：按 Google 文档修网站侧技术阻断（5xx、重定向、robots/noindex 误挡、soft 404、401/403/404、规范网址错位）；按 SMTP 状态码处理退信（5yz 停地址，4yz 交传输重试）；改掉命中 Google 标题 / 摘要缺陷清单的那一处。**收录后零展示、点击率、回复率、跟进次数与间隔、询盘个数、何时上移到按比率改页 / 改序列，均无通用阈值**——这些情形只记账。无回复不构成停在第一封或改写序列的理由（Belkins、Instantly 都显示第一封之后仍有相当比例回复，但 3–5 封与 4–7 封互相冲突，不合成配额）。个位数询盘只记账的 0–9 是字面边界，非业界公布线。规则表每行带承接 skill（均存在于 `skills/`）。

全文：[`research/feedback-action-rules.md`](../research/feedback-action-rules.md)。

主模型抽查（2026-10-14）：RFC 5321 §4.5.4.1「retry interval SHOULD be at least 30 minutes」「give-up time generally needs to be at least 4-5 days」原文一致；Belkins 回复率页 7,530,489 封 / 34,393 回复、定义排除自动回复与退信，原文一致；Google 索引报告「a week or so」「no need to resubmit」「fewer than 500 pages」原文一致；规则表 21 个承接 skill 名全部存在；0.45% 下 100 封零回复概率 0.637 复算一致。
