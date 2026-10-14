---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
blocked_by: []
---

# 外展的合法边界

## Question

「成熟的反馈分级做法」查到：德国 UWG §7 下，无事先明示同意的电子邮件广告构成骚扰（推定同意不适用于邮件）。本仓库获客线的核心外展动作是冷邮件（`lead-cold-email-gen`、`lead-followup-sequence` 等），目标买家是德国/DACH 的光伏储能安装商、EPC、分销商。

- UWG §7 对 **B2B** 冷邮件的确切适用（§7(2)、§7(3) 既有客户例外的条件），有无判例/权威解读界定「可推定同意」在 B2B 邮件上的边界；违规后果（Abmahnung 等）的实际风险。
- 奥地利、瑞士及其他欧盟主要市场对 B2B 冷邮件的规则差异（若获客目标可外扩）。
- 在德国合法的 B2B 获客外展形态：LinkedIn 私信/InMail、B2B 电话（§7(2) 对 B2B 电话的推定同意）、展会、询价平台、先获同意再发信（如 lead magnet 换取 Double-Opt-in）、经分销商/合作方等。每种形态下 L0–L3 反馈能怎么回流。
- 结论要能回答：获客线「闭环」在德国的合法主路径是什么，现仓库哪些 lead skill 的默认动作需要改道。

产出：`wayfinder/feasibility/research/outreach-legal-boundary.md`，每条事实带来源 URL（优先法条原文、法院判决、IHK/律所等权威解读）。这不是法律意见，结论标注需律师确认的点。

## 派工记录

Grok Build 桥接会话 `0def3a9e-ed76-4c1c-922c-6b685895d24a`（2026-10-14 派出）。产出：`wayfinder/feasibility/research/outreach-legal-boundary.md`。

## Resolution

**德国对安装商/EPC/分销商的冷邮件，没有事先明示同意即违法**：UWG §7(2) Nr. 2 的「收件人」不分 B2B/B2C，推定同意只适用于 Nr. 1 的 B2B 电话；公开邮箱、网站「欢迎联系」、LinkedIn 互连都不构成同意。§7(3) 既有客户例外须四项同时成立。后果是警告函（带违约金承诺）与律师费，竞争者、协会、工商会都能主张。LinkedIn 私信/InMail 按电子邮寄对待；仅凭「对方是安装商」打电话也达不到推定同意。奥地利更严（邮件、电话都要事先同意）；法国 CNIL 允许 B2B 反对制，但不能借来向德国发信。

**获客线在德国的合法主路径 = 买家先开口（页面、表单、询盘、来信）+ 先取得可证明的明示同意（如 Double-Opt-in）再由人手动发信；冷邮件不是这条路径。** 默认动作须改道的 skill：`lead-cold-email-gen`、`lead-warm-email-transform`、`lead-followup-sequence`、`lead-email-sequence-strategy`、`lead-targeted-outreach`；`lead-magnet-gen` 跟进稿、`lead-contact-discovery` 名单、`lead-service-first-contact` 未指定通道在发往德国前也要改道。须律师确认的点列在全文末尾（同意文本与 DOI 记录、展会/询价覆盖几封后续信、境外发件管辖等）。非法律意见。

全文：[`research/outreach-legal-boundary.md`](../research/outreach-legal-boundary.md)。主模型抽查（2026-10-14）：§7(2) Nr. 1/Nr. 2 原文与 gesetze-im-internet.de 现行文本一致。
