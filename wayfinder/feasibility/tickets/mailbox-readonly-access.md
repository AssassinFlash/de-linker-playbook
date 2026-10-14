---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
blocked_by: []
---

# 只读邮箱接入

## Question

`chester@de-linker.com` 托管在哪（查 MX/SPF 等公开 DNS 记录），对应的只读接入方式（Gmail API 只读 scope、Microsoft Graph Mail.Read、IMAP 只读）各自最小步骤与坑是什么？如何从收发件里稳定识别：L0 已发出的外展邮件、L2 对外展的回复、L3 询盘来信（含站点表单与形式发票申请触发的通知邮件）？有无成熟开源实现可参照。

产出：`wayfinder/feasibility/research/mailbox-readonly-access.md`，每条事实带来源 URL。

## 派工记录

Grok Build 桥接会话 `d69b4482-237c-4944-b414-06c4168cd37d`（2026-10-14 派出；`grok_status`/`grok_events` 可查）。产出：`wayfinder/feasibility/research/mailbox-readonly-access.md`。

## Resolution

**chester@de-linker.com 托管在腾讯企业邮**（MX mxbiz1/2.qq.com，mail.de-linker.com → exmail.qq.com），不在 Google/Microsoft，Gmail API 与 Graph 用不上；只读路径是 IMAP（imap.exmail.qq.com:993 SSL，EXAMINE + BODY.PEEK，安全登录需客户端专用密码）。L2 回复用 Message-ID 对齐 In-Reply-To/References 并排除自动回复；L0 仍以执行登记为准，邮箱只作已发送核对。**站点询盘通知默认 To sales@（Bcc 线上值未知），读 chester@ 拿不全 L3**——L3 更稳的来源是站点 Woo 数据本身。域名无 DMARC 记录。无开源项目实现这套 L0/L2/L3，可用 ImapFlow / imap_tools 做读取。

全文：[`research/mailbox-readonly-access.md`](../research/mailbox-readonly-access.md)。主模型抽查（2026-10-14）：MX、SPF、mail CNAME 向权威 NS 复查一致；站点 TeamEmail 默认 To sales@ 与代码一致。
