---
name: marketing-retention
description: >
  Use when the user asks for retention strategy, churn prevention, repeat
  order rate, win back dormant clients, referral program, partner commission,
  customer health score, lifecycle marketing, B2B foreign trade retention,
  留存策略, 复购率, 流失预警, 沉默客户挽回, 客户健康度, 生命周期营销, 挽回序列,
  or 转介绍佣金. Collect baseline repeat-order and funnel metrics, score client
  health, design win-back and referral programs, and write a sourced plan
  under deliverables/marketing/06-growth/. Read the ledger product_context
  first; invent no repeat rates, churn counts, or competitor URLs. Never paste
  skill examples into the output. Not for a launch-event GTM, standalone
  inquiry-form redesign, or phase navigation.
---

# 客户留存

根据已读产品上下文与可验证订单/漏斗记录，做复购基线、健康度分层、流失预警、挽回与转介绍，写出可执行的留存计划，落到 `deliverables/marketing/06-growth/`。不写上市事件 GTM，不定稿整页询盘表。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/`、`deliverables/marketing/05-cro/`（落地页、漏斗、询盘流）与 `deliverables/marketing/06-growth/` 中的上市、转介绍稿。从上下文、用户本轮或已有导出列出：近 12 个月活跃客户数与复购率、订单周期与客单价、买家角色与目标市场、询盘→报价→样品→订单、沟通渠道、已知流失原因或沉默客户数。完成：能指出各依据哪几条；原文不拷进本仓库。品类或市场不明、且无订单记录可核则停并写缺口，不编造复购率、流失人数或竞品事实。
3. **采集**。用网页搜索查证制造业留存、流失原因与转介绍做法；需要原文时抓取指定 URL 的正文（本站首页、产品页、询盘页；≥3 个竞品询盘/留存/转介绍页；公开的伙伴页）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；竞品页与流失原因达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据推导生命周期、健康度公式与分层、流失信号、分角色杠杆、询盘摩擦（留存视角）、4 次挽回触达、转介绍结构、ORB 再激活日历。量表、权重与表列见 `references/methodology.md`。完成：健康度四维权重可复述；流失信号 ≥7 且各有检测与响应；挽回 4 触达有时间与角度；推荐人类型 ≥4 或已写缺口。
5. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客短句、URL、字段名、文件名跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造复购或沉默人数。
- 健康度权重固定：订单频次 35%、订单金额 30%、沟通 20%、关系 15%。低于 60 分的客户超过 30% 时，先修订单之间的沟通，不先加积分或会员。
- 行业数字一律标「行业参考值，实际以你的数据为准」。佣金区间在对照真实毛利前不得写成已批准政策。
- 数字、复购率、流失人数只写观察到的值或用户本轮提供的值；没有就写「用户数据未知」并给测量计划，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 这是制造/外贸留存（样品、生产进度、质检、出运、清关），不套用 NPS、功能采用或免费增值。
- 角色从产品上下文取；上下文没有则在指定人、承包、开发商、经销、电商采购里选最贴近的一档，并标明「角色未在上下文出现，暂用」。不要用 C 端消费者口吻，也不对所有角色用同一套杠杆。
- 挽回每触必须带过去订单或项目的具体指代，并给新能力、市场观察或样品中的一项新价值；四次无回应后停放，六个月后再看。
- 转介绍必须有可手填的推荐日志列（邮件或即时通讯介绍记录），禁止只有奖励没有归因。
- 询盘摩擦只写留存相关的入口与首次体验；整页表单改造交给询盘流程 skill 的既有产出，不在此另起一套 CRO。
- `source` 写具体 URL 或用户数据文件名，不写空的能力名。
- 终稿不留未替换占位；品类、市场、产地只引用产品上下文对应字段。

## 产出

路径：

- `deliverables/marketing/06-growth/retention.md`
- `deliverables/marketing/06-growth/retention-strategy.xlsx`（从 `templates/retention-strategy.xlsx` 复制后填；不能写表时改同目录 `retention-strategy.json`）
- 按需同目录：`retention-playbook.md`、`churn-signals.md`、`health-score-model.md`、`win-back-campaigns.md`、`referral-program-design.md`、`inquiry-flow-spec.md`、`reactivation-calendar.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 客户留存

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 客户留存现状诊断

## 流失预警信号系统

## 客户健康度评分模型

## 按买家画像的留存策略

## 询盘流程优化方案

## 挽回序列设计

## 转介绍与合作伙伴计划

## 发布与再激活日历

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿六表：Client Health Score、Churn Signals、Retention Programs、Win-Back Sequence、Referral Program、Inquiry Flow Improvements。每行 `source` 非空。禁止只交空模板。无客户级订单行时仍写出公式、分级与测量计划，客户行标缺口，不编造名单。

## 例子

> 仅供理解，禁止引用到输出。

用户要「提高复购」。输入是已有订单记录、沉默人数未知。写成：按健康度四维打分；流失信号对照安装商留下/拆单的议题形状（到货承诺落空、索赔被推去厂家、没有固定对接人、进价频改导致对方对外报价翻车），各写检测与响应；对 90 天无联系写 4 次触达，每次点名过去订单或项目。不写无来源的「复购率提升 20%」，也不把首单写成整户换商。

用户把赢回写成「替换现有供应商」。写成：安装商侧常见的是按品类拆篮子，首单更像备线开口；材料价是对方利润载体，不用「比现有渠道便宜」当复购杠杆。挽回与转介绍按「哪几条线还在、哪几条已走」分层。

用户把售后当积分会员。写成：店级 FAQ 把保修问句单独分桶后，市场默认是厂家承保、批发商当接口；留存杠杆是交货后是否还在、谁接手案子。不写成自有质保承保或备件库，不把库存与时效承诺当卖点，也不把理赔话术塞进产品页 FAQ（产品页只清临门一脚的订货疑虑，店级采购/发货/退货/账号问句不进那一页）。低于 60 分超过 30% 时先修订单之间的沟通，不加会员。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文、也没有订单或漏斗记录，就套 SaaS 留存清单。
- 编造复购率、沉默人数、佣金效果或竞品 URL。
- 跳过买家分层，对所有角色用同一套动作。
- 健康度改权重或丢掉分级动作。
- 挽回不引用过去订单，或触达不足 4 次。
- 转介绍有奖励无手填归因。
- 忽略样品、生产进度、质检与出运。
- 推荐与现有渠道或小团队运力不兼容的工具。
- 建议未引用采集来源。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 复购率、沉默占比、询盘到订单已采集或已写测量计划
- [ ] ≥3 个竞品询盘/留存/转介绍页，各有 URL
- [ ] ≥5 条经核实的制造业流失或留存原因
- [ ] 健康度权重与四档动作已写出；流失信号 ≥7 且可无独立 CRM 检测
- [ ] 挽回 4 触达有时间、渠道、角度；推荐人类型 ≥4 或已写缺口
- [ ] 主文档与工作簿在 `deliverables/marketing/06-growth/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
