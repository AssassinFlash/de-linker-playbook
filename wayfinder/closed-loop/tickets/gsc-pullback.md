---
wayfinder: task
status: open
assignee:
step: 1
blocked_by: [gsc-site-access, cloud-service-account, execution-log-flow]
---

# GSC 数据回流

## Question

（AFK，开头一步 HITL）仓内脚本把 GSC 数据写进底表：收录（URL Inspection）→ L1；展示 → L1；点击 → L2。依据「Google 渠道接入路径」全文（`wayfinder/feasibility/research/google-channel-access.md`）。

- HITL 前置：操作者在 GSC 把服务账号加为用户（受限权限即可读）。给一步清单。
- 资源标识 `https://de-linker.com/`（带尾斜线），不是 `sc-domain:`。
- 查哪些 URL：执行登记里的 URL ∪ 站点地图里的 URL（URL Inspection 有每资源每日配额，按官方文档取值，超额时优先执行登记里的）。
- Search Analytics 按页 × 日期取展示 / 点击 / 排名；数据晚 2–3 天，脚本要可重跑、按日期幂等（不重复追加）。
- 定时：本票定一个方案并装好（如操作者 Mac 的 launchd，或服务 VPS 的 cron），写清怎么看它跑没跑、怎么停。断档风险记入 Resolution。

## 完成标准

- 底表网页反馈表有真实行（至少一个页面的收录状态与近 7 天展示）；重跑一次不产生重复行；定时任务至少自动跑过一次（看日志）。
