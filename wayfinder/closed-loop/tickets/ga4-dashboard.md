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

## 站点接入交接（2026-10-19 已完成）

用户已裁定日常账号与服务账号均为管理员：日常账号为 GA4 账号层管理员，服务账号为 de-linker 媒体资源管理员，取代先前“服务账号只给查看者”的安排。资源真实值与授权读回记录见私有 vault `marketing/00-system/ga4-owner-checklist.md`。

- 站点接入票已关闭：新站 [GA4 与 CookieYes 接入](https://github.com/AssassinFlash/de-linker/pull/358) 已生产部署并读回，GA4 实时报告看到实际同意后的访问；CookieYes 英德版本已上线。现有 Search Console 保持。
- **两项可独立选择**：Website analytics / Website-Analyse 决定 GA4；Visit source / Besuchsquelle 决定原生 Woo `sbjs_*`。只同意来源不向 Google 发事件；来源用途的内部 WP Consent API 类别虽叫 marketing，三个 Google Ads 同意信号始终 denied。
- 拒绝前/后及撤回后完全不向 GA4 发追踪请求，故只统计同意分析的访客，无建模补齐；不能用 GSC 点击与 GA4 访问直接对账。
- 事件保留 14 个月；增强衡量与 Site Kit 原生插件转化跟踪启用，已排除全部登录用户。Google Signals、用户提供数据、广告个性化关闭。本票须另验询盘相关事件是否真实触发及可归因，不因 Site Kit 配置显示 Enabled 就当它已完成。
- 完成证据在上述私有清单末节与 `marketing/00-system/evidence/2026-10-19-ga4/`。站点上线执行登记为 `E-20261019-01` 至 `E-20261019-04`。这些是本票的前置事实，本票本身仍未执行。
