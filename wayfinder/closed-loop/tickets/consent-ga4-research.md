---
wayfinder: research
status: open
assignee: grok-build (dispatched 2026-10-14)
grok_session: dc74cb2e-73e7-4692-86ff-92c7938bdf2a
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
