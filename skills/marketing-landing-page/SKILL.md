---
name: marketing-landing-page
description: >
  Use when the user asks for landing page, CRO, conversion rate optimization,
  inquiry form, popup, funnel optimization, inquiry flow, launch strategy,
  referral program, retention, B2B foreign trade, 着陆页, 落地页, 转化率优化,
  询盘表单, 弹窗, 询盘流程, 启动策略, 转介绍, or 客户留存. Audit live homepage,
  product, and inquiry pages against competitor CTAs, forms, and trust
  signals; write a sourced page audit, form redesign, popup plan, and
  experiment queue under deliverables/marketing/05-cro/. Read the ledger
  product_context first; invent no conversion rates, field counts, or
  competitor URLs. Never paste skill examples into the output. Not for
  paid-media plans, technical site rebuilds, or phase navigation.
---

# 着陆页

根据已读产品上下文与可抓取页面，审计首页、产品页与询盘页的主张、CTA、表单与信任信号，写出可执行的改写与实验队列，落到 `deliverables/marketing/05-cro/`。不定稿付费投放，不做整站技术重构。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/` 与 `deliverables/marketing/02-seo/seo-audit.md`。列出品类、目标市场、买家角色、流量来源、询盘渠道、建站平台约束、漏斗已知转化率。完成：能指出各依据哪几条；原文不拷进本仓库。用户只给站点 URL 时先抓该站再补上下文；品类或市场仍不明则停并写缺口，不编造公司、转化率或竞品事实。
3. **范围**。本 skill 主责页面级转化：着陆页审计、CTA、表单字段、弹窗、实验队列。用户只要询盘整条路径则打开 `skills/marketing-inquiry-flow/SKILL.md`；只要上市事件则打开 `skills/marketing-launch-strategy/SKILL.md`；只要转介绍或留存则打开对应方法 skill。需要隔离时 dispatch a subagent, else do it inline。完成：主责与他 skill 边界各写一句，不在本工作簿加上市/转介绍/留存表。
4. **采集**。用网页搜索查证 B2B 着陆页与询盘表做法；需要原文时抓取指定 URL 的正文（本站首页、产品/服务页、询盘页、下单流程页；≥3 个竞品首页+产品页+询盘页）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；本站三页与竞品对照达到最低条数，或已把未达标项写入缺口。
5. **分析**。只从已采集证据给页面 1–5 分、表单字段对照、弹窗规格、实验假设。量表、漏斗与表列见 `references/methodology.md`。完成：每个 P0 能指到已抓取页面；P0 文案有 before → after；行业数字已标「行业参考值，实际以你的数据为准」。
6. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客标题、按钮、URL、字段名、文件名跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造询盘量或转化率。
- 这是制造/外贸询盘（询盘、报价、样品），不套用试用开通、加入购物车或限时秒杀。
- 数字、转化率、字段数、响应时长只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」。行业数字一律标「行业参考值，实际以你的数据为准」。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 先抓再改。没有已抓取正文，不写页面建议。
- 建站平台、主题、表单插件限制必须约束建议；上下文未写明则记缺口，不假设某一建站产品。
- 询盘表桌面 5–7 字段、移动端压到约 3–4 个；按钮写行动加结果，不用空的 Submit。
- 即时通讯入口是否启用、放在哪些页，以目标市场与产品上下文已出现频道为准。
- 角色从产品上下文取；上下文没有则在采购、承包、指定人、经销、质量/合规里选最贴近的一档，并标明「角色未在上下文出现，暂用」。
- `source` 写具体 URL，不写空的能力名。终稿不留未替换的占位符。
- 佣金或加售建议必须能对上产品上下文的毛利结构；对不上则记缺口，不写比例。

## 产出

路径：

- `deliverables/marketing/05-cro/landing-page.md`
- `deliverables/marketing/05-cro/cro-experiment-queue.xlsx`（从 `templates/cro-experiment-queue.xlsx` 复制后填；不能写表时改同目录 `cro-experiment-queue.json`）
- 按需同目录：`page-audit-findings.md`、`copy-rewrites.md`、`form-field-spec.md`、`popup-designs.md`、`ab-test-plan.md`

章节与表列、最低行数见 `references/methodology.md`。询盘规格、回复模板、上市时间线、转介绍设计、留存手册不在本 skill 落盘。

```markdown
# 着陆页

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 现状审计

## 竞品 Benchmark

## 着陆页优化方案

## 表单与询盘入口方案

## 弹窗与 Lead Capture 方案

## KPI 追踪计划

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿五表：Experiments（≥10 行）、Results（测试后填，可为 0 行）、Page Audit（≥5 行）、Form Redesign（≥8 行）、Popup Plan（≥6 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「优化着陆页 CTA」。写成：已抓取首页首屏标题与按钮原文，P0 给出 before → after，并把 URL 写入 `source`；不写无来源的「转化率提升 30%」，也不把本节句子粘进交付物。

## 易错

- 没读产品上下文、也没抓本站页面，就套通用 CRO 清单。
- 只审首页，跳过产品页和询盘页。
- 用 Competitor A/B/C 占位，或不记录必填字段数与 CTA 原文。
- 编造转化率、字段数或竞品 URL。
- 建议「优化 CTA」却不给 before → after。
- 表单字段只增不减，或移动端仍超过约 4 项必填。
- 弹窗无频率上限、无退出意图，对采购研究页无差别打断。
- 把试用、购物车、秒杀等 C 端话术写进外贸询盘页。
- 行业基准未标「行业参考值，实际以你的数据为准」。
- 在本工作簿加上市、转介绍或留存表。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 本站首页、产品/服务页、询盘页已抓取且可访问
- [ ] ≥3 个竞品页：CTA、信任信号、表单结构均有来源 URL
- [ ] ≥2 个竞品询盘表：字段数、必填、CTA 原文已摘录
- [ ] 每个 P0 有 before → after 并引用已抓取页
- [ ] Experiments ≥10 行、Page Audit ≥5、Form Redesign ≥8、Popup Plan ≥6；每行 `source` 非空
- [ ] 行业数字已标「行业参考值，实际以你的数据为准」
- [ ] 主文档与工作簿在 `deliverables/marketing/05-cro/`；无上市/转介绍/留存表
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
