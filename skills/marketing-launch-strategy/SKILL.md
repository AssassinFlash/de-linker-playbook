---
name: marketing-launch-strategy
description: >
  Use when the user needs a new product launch, new market entry, trade-show
  debut, website launch, new capability launch, GTM plan, launch timeline,
  channel plan, post-launch growth plan, 上市策略, 发布计划, or 展会上市. Collect
  market and competitor evidence, then write a three-phase launch plan that
  connects positioning, channels, landing pages, inquiry handling, referral
  loops, and retention, with owners, dates, and sources. Read the ledger
  product_context first; invent no company, market, pricing, or competitor
  facts. Output under deliverables/marketing/06-growth/. Not for evergreen
  retention without a launch event, not for pure paid-media planning, and
  not for phase navigation.
---

# 上市策略

把定位、渠道、落地页、询盘、推荐与留存收成一份可执行的上市计划，写到 `deliverables/marketing/06-growth/`。无上市事件的常青留存、纯付费投放，不走本文件。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。列出上市类型、目标买家、市场、日期或展会、样品就绪、贸易条款、当前漏斗指标。上游若存在则读 `deliverables/marketing/01-foundation/`、`03-content/`、`05-cro/`。完成：能指出受众与约束各依据哪几条陈述；缺项写成缺口清单后停，不编造公司、市场、价格、流量或竞品事实。原文不拷进本仓库。
3. **范围**。判定类型（新产品 / 新市场 / 展会 / 网站 / 新能力）与规模（major / medium / minor）。完成：类型与规模各有一句可辩护理由，能回溯上下文或已采集来源。
4. **采集**。用 Apify 搜索查证上市框架、展会日历、竞品宣布、目标市场渠道偏好；需要原文时抓取指定 URL（用户落地页、询盘页、至少 3 个竞品页）。查询意图与最低条数见 `references/methodology.md`。多页抓取需要隔离时 dispatch a subagent, else do it inline。完成：每条证据有 URL、摘录、访问日期；Apify 修复与替代取证后仍不可得则停止并写缺口。
5. **设计**。按 Pre-Launch / Launch Week / Post-Launch 写任务，含责任人、依赖、证据；日期写成日历日或 T-xx / T-day / T+xx（禁止只写 Week 1）。渠道用 ORB（Owned / Rented / Borrowed），名单以产品上下文为准，不默认某一电商平台。完成：三阶段都有具体日期；每条渠道建议能回溯采集来源。
6. **映射**。接到落地页与询盘流、推荐/伙伴动作、复购培育。用户给了 URL 时，CRO 建议必须来自已抓取正文。评分表、表结构或执行附件规格读 `references/methodology.md`。完成：询盘入口、响应时限、至少 3 类推荐人、流失信号均已写上。
7. **落盘**。写入下方路径。完成：主文档与工作簿非空；每条对外建议有 `source`；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客文案、URL、文件名、脚本语种以产品上下文为准，同一段不混用。
- 目标渠道以产品上下文为准。未写明时按 ORB 三类各给可执行动作，不默认某一平台。
- 贸易条款写清 Incoterms（FOB 出运地 / CIF 目的港以产品上下文为准）与支付方式。
- 样品与物流写进时间线：规格、包装、海运或空运周期、海关文件。
- 展会名称与日期须核官方源；不写未核验的届次或人流。
- 缺来源或Apify 修复与替代取证后仍不可得：停止并写缺口，不编造。

## 写法

- 制造/外贸约束（样品重量、包装、清关、运输周期）必须约束时间线，不套用 SaaS 的 freemium 或应用商店优化。
- 多变体错开宣布，间隔约 1–2 周，不一次铺开。
- 询盘表桌面 5–7 字段、移动端压到约 4 个；按钮写行动加结果，不用空的 Submit。
- 即时通讯入口（如 WhatsApp / WeChat）是否启用以目标市场为准，不默认只走邮件。
- 推荐至少问「How did you hear about us?」，并准备可手填的推荐日志列。

## 产出

路径：

- `deliverables/marketing/06-growth/launch-strategy.md`
- `deliverables/marketing/06-growth/launch-strategy.xlsx`（从 `templates/launch-strategy.xlsx` 复制后填 Timeline、Channels；其余 sheet 按 `references/methodology.md` 补齐）
- 可选：`deliverables/marketing/06-growth/launch-strategy.json`
- 执行附件按需，同目录

```markdown
# 上市策略

- launch_type:
- scale: major | medium | minor
- source: 台账 product_context（不粘贴原文）
- accessed:

## 类型与规模

## 目标市场与买家矩阵

## 三阶段计划

## 渠道（ORB）

## 落地页与漏斗审计

## 询盘流

## 推荐计划

## 留存与上市后培育

## 样品与物流清单

## 行动清单（P0 / P1 / P2）

## 可验证断言
```

工作簿每行必须有非空 `source` 或 `evidence`。未提供 URL 的审计表写缺口，不拿通用最佳实践充数。

## 例子

> 仅供理解，禁止引用到输出。

输入写「下个月展会上市」。计划写成：T-6 周寄样并做预展约访、开展当天扫码进 CRM、24 小时内跟进询盘；渠道可把自办行业日写成一场有日期的 Owned 动作。不写无日期的「全面铺开线上线下整合营销」，也不把库存灯号或运达时效当展台卖点。

输入写「网站按欧洲批发平台重做后上线」。成稿应对照两种格局——公开目录+锁价（店内一体）vs 宣传站+登录门户（硬拆）——写清本站选哪一种、注册是一次核验还是每单人工闸、品类×品牌与套餐是否当一等公民。改版用「当前线上 | 最终替换」分列，散文可重建、规格数据区默认保留。不把竞品首页口号抄进时间线，不用过时品类规模数字当论据，也不把一站式/去中间商套话当发布主题。

输入写「发布自有规划工具，对标设计软件」。成稿应把能力放进交易格（可询价、可下单的物料清单），标明仿真格 / 排布格 / 经济优化格买家已有座位、本发布不替换那些座位。不把战役写成规划软件或可融资报告，不承诺自有质保或制造商身份；上市页只清已有订货阻碍，不种新疑虑。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文就套通用上市稿。
- 把教学例子或无来源假设当事实。
- 只交 Markdown、工作簿仍是空模板。
- 时间线只写 Week 1 / Week 2，没有日历日或 T-xx。
- 用户给了 URL 却不抓取正文，直接给 CRO 建议。
- 多变体同一天全发。
- 忽略样品就绪与物流周期。
- 推荐有奖励无归因。
- 把展会只当曝光，没有预展约访与当日录入闭环。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 类型与规模可辩护；三阶段有具体日期
- [ ] 渠道匹配产品上下文，且 ORB 三类都有动作
- [ ] 样品、物流、贸易条款已量化
- [ ] 有 URL 则审计来自已抓取正文
- [ ] 推荐 ≥3 类；留存含流失信号与触点日历
- [ ] 主文档与工作簿在 `deliverables/marketing/06-growth/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
