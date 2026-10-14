---
wayfinder: task
status: open
assignee:
step: 5
blocked_by: [ga4-consent-site-access, looker-dashboard]
---

# GA4 进看板

## Question

（HITL：操作者按指南做）把 GA4 接进看板与（如需要）底表。

- 先定：GA4 只用 Looker Studio 原生连接器直接上看板，还是也经 GA4 Data API 写进底表（让 AI「下一步」能读到）。取决于「反馈分级规则定稿」里是否有用到站内行为的规则；没有就只上看板。
- 看板加 GA4 版面（访问、来源、着陆页、询盘相关事件若有），注明「只含同意了的访客，数字偏低」。更新 `docs/` 指南。

## 调研交接（「同意横幅与 GA4 选型调研」关票时写入）

- 站点按 Consent Mode **Basic** 接入：拒绝的访客在 GA4 里**完全没有事件**，也达不到 GA4 行为建模资格（需 Advanced + 每日 1,000 事件 / 用户门槛）。看板与指南要写明「GA4 只含同意了的访客、无建模补齐」，不要拿它和 GSC 点击数对账。

## 完成标准

- 操作者能在看板上说出近 7 天访问量与主要来源，并知道为什么它比真实访问少。
