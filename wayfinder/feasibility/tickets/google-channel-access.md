---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
blocked_by: []
---

# Google 渠道接入路径

## Question

用「仓内脚本，任何 harness 能跑」的方式，把 GSC、GA4、Google Sheets 打通成反馈回流的最小已验证路径是什么？

- GSC Search Analytics / URL Inspection / Sitemaps API：授权方式（服务账号 vs OAuth 用户）、配额、数据延迟与保留期、冷启动站点（零或极少展示）能拿到什么。现成实现（如 AminForou/mcp-gsc、官方/社区脚本）是否成熟可直接用。
- GA4 Data API：同上；以及在德国（GDPR/TTDSG）上 GA4 的法定前提（同意横幅、Consent Mode v2）与 WordPress 上主流同意方案；无 Cookie 替代（Plausible、Matomo 无 Cookie 模式等）能否替代、代价。
- Google Sheets API：脚本追加行与读规则的授权与配额；与 GSC/GA4 共用一套 Google 凭据是否可行；Looker Studio 原生连接器作为「现成看图」是否零开发。
- 每条给：最小步骤、所需账号权限、已知坑、来源 URL。

产出：`wayfinder/feasibility/research/google-channel-access.md`。

## 派工记录

Grok Build 桥接会话 `af802248-b17e-45b5-907a-3405dc64c747`（2026-10-14 派出；`grok_status`/`grok_events` 可查）。产出：`wayfinder/feasibility/research/google-channel-access.md`。

## Resolution

最小已验证路径 = 1 个 Cloud 项目 + 1 把服务账号密钥（仓库外）+ GSC/GA4/Sheets 三处分别授权该服务账号 + 1 个仓内 Python 脚本（官方客户端）：读表格里的执行登记 → 查 Search Analytics（展示→L1、点击→L2）与 URL Inspection（收录）→ 追加回表格；系统定时任务驱动，GSC 数据晚 2–3 天。GSC 不在访客端写 Cookie，无同意前提；**GA4 在德国须先有同意横幅**，Consent Mode v2 不替代横幅；无 Cookie 统计只能替代站内浏览，替代不了 GSC。Looker Studio 原生连接三者、零开发看图。mcp-gsc 有可运行代码但属 MCP，不作为跨 harness 主路径。Indexing API 不适用于普通页面。

全文：[`research/google-channel-access.md`](../research/google-channel-access.md)。主模型抽查（2026-10-14）：URL Inspection、Indexing API 适用范围与官方文档一致。
