---
name: marketing-funnel-optimization
description: >
  Use when the user asks for full-funnel optimization, stage drop-off,
  cross-stage priority, Visit-to-Referral mapping, 全链路漏斗, 阶段流失,
  跨阶段优先级, or 漏斗优化 across Visit through Inquiry, Quote/Sample,
  Order, Repeat, and Referral. Read approved 05-cro page and inquiry
  deliverables; crawl the live site only to flag contradictions and
  gaps; write a sourced cross-stage plan under
  deliverables/marketing/05-cro/. Read the ledger product_context first;
  invent no conversion rates or competitor URLs. Never paste skill
  examples into the output. Not for a single-page layout pass, post-submit
  reply scripts, standalone launch/referral/retention playbooks,
  paid-media plans, or phase navigation.
---

# 漏斗优化

根据已读产品上下文与可抓取页面，把 `Visit → Inquiry → Quote/Sample → Order → Repeat → Referral` 全链路对照已批准的 `landing-page.md` 与 `inquiry-flow.md`，只填跨阶段矛盾、缺口与优先级，落到 `deliverables/marketing/05-cro/`。不定稿付费投放，不导航阶段。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/`、`deliverables/marketing/03-content/` 与 `deliverables/marketing/05-cro/` 已批准的 `landing-page.md` 与 `inquiry-flow.md`（缺则记缺口，不重做页上入口或提交后话术）。列出品类、买家角色、目标市场、贸易条款、样品政策、询盘量、询盘→报价/样品/订单、复购率、主要流失阶段、已用渠道。完成：能指出各依据哪几条；原文不拷进本仓库。用户只给站点 URL 时先抓该站再补上下文；品类或市场仍不明则停并写缺口，不编造公司、转化率或竞品事实。
3. **采集**。用网页搜索查证漏斗优化与行业基准；需要原文时抓取指定 URL 的正文（本站首页、产品页、询盘页、落地页；≥3 个竞品完整漏斗）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；本站四页与竞品漏斗达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据与已批准稿映射漏斗各阶段。第 3–6 章（落地页/表单/弹窗/询盘流）读已批准的 `landing-page.md` 与 `inquiry-flow.md`，只填跨阶段矛盾与缺口，不重做 CTA、字段清单或回复话术。第 9–11 章（上市/转介绍/留存）指向 `marketing-launch-strategy` / `marketing-referral-program` / `marketing-retention` 的既有产出，本 skill 只写跨阶段优先级。资质量表与询盘稿不一致时以 `inquiry-flow.md` 七维四档为准。量表、漏斗与表列见 `references/methodology.md`（与本节冲突时以本节为准）。完成：每个 P0 建议能指到已抓取页面或已批准稿；12 个主文档章节均有着落或显式缺口；升级报价保留基础选项。
5. **落盘**。写入下方路径。已有 `funnel-optimization.md` 则增量更新并在文首保留版本说明。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；URL、字段名、CTA copy、文件名用英文。面客短句跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造询盘量或转化率。
- 主转化是 RFQ / inquiry 与订单，不是试用开通或套餐升级。
- 首次回复的方法默认目标：工作时间内 2 小时。与已批准 `inquiry-flow.md` 不一致时以询盘稿为准。行业数字一律标「行业参考值，实际以你的数据为准」。
- 资质量表以已批准 `inquiry-flow.md` 的七维四档为准，不在本文件另开一套。
- 数字、转化率、回复时长只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 这是制造/外贸漏斗，不套用试用、激活、套餐升级话术。
- 表单字段、CTA、回复话术以已批准 `landing-page.md` 与 `inquiry-flow.md` 为准；本 skill 只标跨阶段矛盾与缺口，不重写字段清单或话术。
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
- 按需同目录：`landing-page-audit.md`、`form-redesign-spec.md`、`popup-designs.md`、`inquiry-flow-spec.md`、`onboarding-playbook.md`、`upsell-playbook.md`、`launch-timeline.md`、`referral-program-design.md`、`retention-playbook.md`、`ab-test-plan.md`（不替代已批准的 `landing-page.md`、`inquiry-flow.md` 或 `06-growth/` 下上市/转介绍/留存正文）

章节与表列、最低行数见 `references/methodology.md`。第 3–6 章读已批准的 `landing-page.md` 与 `inquiry-flow.md`，只填跨阶段矛盾与缺口，不重做 CTA/字段/回复话术。第 9–11 章指向 `marketing-launch-strategy` / `marketing-referral-program` / `marketing-retention` 的既有产出，本 skill 只写跨阶段优先级。

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

工作簿七表：Funnel Analysis（≥7 行）、Experiments（≥15 行）、Page Audit（≥5 行）、Form Benchmark（≥5 行）、Launch Timeline（≥15 行）、Referral Program（≥5 行）、Retention Signals（≥8 行）。每行 `source` 非空。禁止只交空模板。Page Audit / Form Benchmark 引用 `landing-page.md` 与已抓页面，不另起 CTA 或字段定稿；Launch Timeline / Referral Program / Retention Signals 引用对应 skill 既有产出路径，缺则缺口，不重写佣金或赢回正文。

## 例子

> 仅供理解，禁止引用到输出。

输入写「优化转化漏斗」。成稿应改成：已抓首页/产品/询盘页，按 Visit → Inquiry → Quote/Sample → Order → Repeat → Referral 标阶段流失；≥3 家竞品记下字段数与 CTA 原文，并标出门的形状——公开目录+锁价（店内一体）对手册站+门户墙、注册一次后自助下单对每单人工审；户用流量记成 Visit 漏向（导向找安装商），不做成贸易结账；一条 P0 带 hypothesis 与 metric。不写无来源的「转化率提升 30%」，也不把本节句子粘进交付物。

输入写「简化注册就能涨转化」。成稿应改成：对照贸易店账户形状，把贸易证明上传、人工审批、行业分拣、送货约束收进一次注册门；审批时长只写公开页已声明的天数或「未声明」。不要拆掉资格门去仿 C 端一键下单，也不把竞品「上传以加快开通」的原句或等待时长写成自己的 SLA。

输入写「加规划器、库存灯、次日达提高下单」。成稿应改成：Quote 阶段只问规划输出能否进购物车或保存报价（交易格，不是仿真报告）；Order 阶段把「颜色灯 vs 日期」「状态停住」记成流失证据。可用性只引用产品上下文已有表述，不把竞品交期、仓库灯或库存数字当卖点。

输入写「表单越短越好、整页重做」。成稿应改成：列出删/留/改字段名；分拣（安装商 / EPC / 批发）留一次，公司证明不在每单重复；用当前线上 | 最终替换对照（保留可核验 CTA，改掉无来源承诺，缺口单列）。不用 Competitor A/B/C 占位；不把过时首页稿或证言三则当线上形状；Repeat/Referral 不承诺制造商质保、备件库或自有承保，也不把交货后沉默当成正常漏斗。

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
- 已有着陆页或询盘稿仍重做 CTA、字段或回复话术。
- 把上市、转介绍、留存从零写一遍，而不引用对应 skill 产出。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 已读已批准 `landing-page.md` 与 `inquiry-flow.md`（缺则缺口，未重做）
- [ ] 本站首页、产品页、询盘页、落地页已抓取（无落地页则记缺口）
- [ ] ≥3 个竞品完整漏斗：落地页、表单、CTA、信任信号
- [ ] 主文档 12 章均有着落或显式缺口；每条 P0 能指到已抓取 URL 或已批准稿
- [ ] 第 3–6 章只填跨阶段矛盾与缺口，无重做的 CTA/字段/回复话术
- [ ] 第 9–11 章指向 `marketing-launch-strategy` / `marketing-referral-program` / `marketing-retention` 既有产出或显式缺口
- [ ] 资质量表与询盘稿不一致处已注明以 `inquiry-flow.md` 七维四档为准
- [ ] 升级报价保留基础选项
- [ ] 主文档与工作簿在 `deliverables/marketing/05-cro/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
