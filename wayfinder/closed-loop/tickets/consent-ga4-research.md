---
wayfinder: research
status: closed
assignee: grok-build (dispatched 2026-10-14)
grok_session: dc74cb2e-73e7-4692-86ff-92c7938bdf2a
resolved: 2026-10-14
step: 5
blocked_by: []
---

# 同意横幅与 GA4 选型调研

## Question

（派 Grok Build；只调研不动站点——站点改动排在 GSC 之后）在 de-linker.com 上合法地装 GA4，最合适的同意横幅与接入方式是什么？

约束（来自新站 `~/Documents/de-linker/AGENTS.md`）：不买付费插件；不走 Code Snippets；EN/DE 双语（Polylang）；德语 Sie 体；客户可见文案走对抗评审；复刻面像素零差异（横幅是「裁定过的变更」，须进变更台账）；LiteSpeed 缓存；WordPress + WooCommerce。若「GSC 站点接入」已关且用了 Site Kit，以其交接为前提。

须查清：

1. 德国（TDDDG §25 + GDPR）对分析类 Cookie 的同意要求：横幅必须有什么（拒绝与接受同级、事先阻断、可撤回、记录）；有出处（监管机构 / 法条 / 判例）。
2. Consent Mode v2：基本 / 高级模式区别；不替代横幅（已有结论，复核即可）；对 GA4 数据缺口的影响。
3. 免费 CMP 候选（如 Complianz 免费版、CookieYes 免费版、Real Cookie Banner 免费版等，主动扩展）：是否支持 Consent Mode v2、WP Consent API、Site Kit 联动、Polylang 双语、事先阻断、无需付费即合规；维护状态。
4. GA4 接入载体：Site Kit vs 仓库插件直接输出 gtag；与所选 CMP 的配合。
5. 推荐组合 + 理由 + 已知坑。

产出：`wayfinder/closed-loop/research/consent-ga4.md`，每条事实带来源。查不到标〔未证实〕。

## 完成标准

- 五问各有结论 + 来源；主模型抽查至少两条（一条法条 / 监管来源、一条插件官方文档），写进 Resolution，并向用户汇报。

## Resolution

推荐 **Complianz 免费版（横幅 + Script Center 事先阻断）+ WP Consent API + Site Kit（GA4 载体，也可作 GSC 载体）**；Site Kit 开 Consent Mode（默认全 `denied`），**不开** Complianz 自己的 Consent Mode（在 Premium，且 Site Kit 文档警告双开冲突）；Script Center 在 statistics 同意前挡住 Google 域名脚本 → 落到 Google 定义的 **Basic**（同意前不传任何数据、拒绝者不发 cookieless ping）。依据：TDDDG §25 + DSK 指南 1.2 边号 (36)(121)(122)「同意先于终端访问」；Advanced 拒绝期间仍发含 User Agent / Referrer 的 ping，与之不合。第一层必须同等的「接受 / 拒绝」（科隆高院 6 U 80/23、汉诺威行政法院 10 A 5385/22）。代价：Basic 无 GA4 行为建模，GSC 仍是 L1/L2 主路径，可接受。备选 CookieYes（文档最齐，但云日志、免费 5,000 PV/月、品牌锁定）；Cookiebot（50 子页）、Cookie Notice（1,000 访问/月后暂停阻断）免费档不够本站。

全文：[`research/consent-ga4.md`](../research/consent-ga4.md)。

主模型抽查（2026-10-14）：TDDDG §25(1) 原文一致；Complianz trunk readme（7.5.6）Script Center / Proof of Consent 在 Premium 标题之前、Google Consent Mode 在 Premium 列表、FAQ「script blocking … no consent record limits」一致；Site Kit Consent Mode 文档点名 Complianz / Cookiebot / CookieYes、「不启用则 EEA/瑞士/英国跟踪被挡」一致。补一处调研漏看：Complianz changelog 有「Google Tag Gateway support — Consent Mode is now applied correctly when Google Analytics or Google Tag Manager loads through a first-party Tag Gateway URL」，与〔未证实〕里的 Tag Gateway 拦截问题相关，仍须实测。

**现状发现**：线上首页已在无同意横幅的情况下加载 WooCommerce 订单归因（Sourcebuster，`sbjs_*` Cookie）；按 DSK 边号 (80) 这组不属于绝对必要。已写进「GA4 与同意横幅站点接入」，由该票一并纳入横幅管理。
