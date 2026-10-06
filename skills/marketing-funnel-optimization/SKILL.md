---
name: marketing-funnel-optimization
description: >
  Use when the user asks for funnel optimization, conversion rate, landing
  page, inquiry flow, RFQ process, form optimization, popup, exit intent,
  launch strategy, go-to-market, referral program, partner program, retention,
  churn prevention, B2B foreign trade, 漏斗优化, 询盘流程, 表单优化, 弹窗,
  发布策略, 转介绍, or 客户留存. Map Visit through Inquiry, Quote/Sample, Order,
  Repeat, and Referral; crawl the live site and competitor funnels; write a
  sourced CRO plan under deliverables/marketing/05-cro/. Read the ledger
  product_context first; invent no conversion rates or competitor URLs. Never
  paste skill examples into the output. Not for a single-page layout pass,
  paid-media plans, or phase navigation.
---

# 漏斗优化

根据已读产品上下文与可抓取页面，把 `Visit → Inquiry → Quote/Sample → Order → Repeat → Referral` 全链路审计并写出可执行修复，落到 `deliverables/marketing/05-cro/`。不定稿付费投放，不导航阶段。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/`、`deliverables/marketing/03-content/` 与 `deliverables/marketing/05-cro/` 已有落地页或询盘稿。列出品类、买家角色、目标市场、贸易条款、样品政策、询盘量、询盘→报价/样品/订单、复购率、主要流失阶段、已用渠道。完成：能指出各依据哪几条；原文不拷进本仓库。用户只给站点 URL 时先抓该站再补上下文；品类或市场仍不明则停并写缺口，不编造公司、转化率或竞品事实。
3. **采集**。用网页搜索查证漏斗优化与行业基准；需要原文时抓取指定 URL 的正文（本站首页、产品页、询盘页、落地页；≥3 个竞品完整漏斗）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；本站四页与竞品漏斗达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据映射漏斗各阶段、落地页、表单、弹窗、询盘流、首单、升级报价、上市、转介绍、留存与实验优先级。量表、漏斗与表列见 `references/methodology.md`。完成：每个 P0 建议能指到已抓取页面；12 个主文档章节均有着落或显式缺口；升级报价保留基础选项。
5. **落盘**。写入下方路径。已有 `funnel-optimization.md` 则增量更新并在文首保留版本说明。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；URL、字段名、CTA copy、文件名用英文。面客短句跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造询盘量或转化率。
- 主转化是 RFQ / inquiry 与订单，不是试用开通或套餐升级。
- 首次回复的方法默认目标：工作时间内 2 小时。行业数字一律标「行业参考值，实际以你的数据为准」。
- 数字、转化率、回复时长只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 这是制造/外贸漏斗，不套用试用、激活、套餐升级话术。
- 改表单必须写出删/留/改的字段名，不写空的「简化表单」。
- 即时通讯入口是否启用、放在哪些产品页，以目标市场与产品上下文已出现频道为准。
- 升级报价必须保留基础选项，且每条报价最多一个清晰升级建议。
- 每个跟进触点必须带可核验的价值点，禁止空的问候。
- 角色从产品上下文取；上下文没有则在采购、承包、指定人、经销、质量/合规里选最贴近的一档，并标明「角色未在上下文出现，暂用」。
- `source` 写具体 URL，不写空的能力名。
- 终稿不留未替换的 `{{...}}` 占位；品类、市场、产地只引用产品上下文对应字段。

## 产出

路径：

- `deliverables/marketing/05-cro/funnel-optimization.md`
- `deliverables/marketing/05-cro/funnel-redesign.xlsx`（从 `templates/funnel-redesign.xlsx` 复制后填；不能写表时改同目录 `funnel-redesign.json`）
- 按需同目录：`landing-page-audit.md`、`form-redesign-spec.md`、`popup-designs.md`、`inquiry-flow-spec.md`、`onboarding-playbook.md`、`upsell-playbook.md`、`launch-timeline.md`、`referral-program-design.md`、`retention-playbook.md`、`ab-test-plan.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 漏斗优化

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 漏斗现状评估

## 竞品漏斗对比

## 落地页优化建议

## 询盘表单优化方案

## 弹窗与潜客捕获策略

## 询盘流程优化方案

## 首单 onboarding 方案

## 升级与交叉销售策略

## 发布上市计划

## 转介绍与合作伙伴计划

## 留存与流失预防策略

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿七表：Funnel Analysis（≥7 行）、Experiments（≥15 行）、Page Audit（≥5 行）、Form Benchmark（≥5 行）、Launch Timeline（≥15 行）、Referral Program（≥5 行）、Retention Signals（≥8 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「优化转化漏斗」。写成：已抓取首页/产品/询盘页的阶段流失、≥3 家竞品字段数与 CTA 原文、一条带 hypothesis 与 metric 的 P0 实验；不写无来源的「转化率提升 30%」，也不把本节句子粘进交付物。

## 易错

- 没读产品上下文、也没抓本站页面，就套通用 CRO 清单。
- 把试用开通、激活漏斗直接搬到询盘与订单。
- 用 Competitor A/B/C 占位，或不记录字段数与 CTA 原文。
- 编造转化率、回复时长或竞品 URL。
- 忽略目标渠道的表单与页面限制。
- 升级报价删掉基础选项，或一次推多个升级。
- 跟进只有客套问候。
- `source` 只写搜索、不附 URL。
- 行业基准未标「行业参考值，实际以你的数据为准」。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 本站首页、产品页、询盘页、落地页已抓取（无落地页则记缺口）
- [ ] ≥3 个竞品完整漏斗：落地页、表单、CTA、信任信号
- [ ] 主文档 12 章均有着落或显式缺口；每条 P0 能指到已抓取 URL
- [ ] 表单有逐字段规格；升级报价保留基础选项
- [ ] 留存含流失信号、health score、≥4 步赢回
- [ ] 主文档与工作簿在 `deliverables/marketing/05-cro/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
