---
name: marketing-product-profile
description: >
  Use when the user says profile, product context, product profile,
  positioning, target audience, ICP, describe my product, 产品档案,
  产品上下文, or 产品定位; when B2B trade marketing needs a deep product
  read of specs, value chain, personas, or proof points; or when the
  product file looks missing, outdated, or incomplete. Read the ledger
  product_context (default ~/Documents/New/CONTEXT.md). If parameters
  are still missing, read fact-base/. Check coverage against the
  fifteen-section checklist; research or interview only to flag gaps.
  Never copy the product archive into this repo. Not for conversion
  copy, SEO audits, campaign plans, or phase navigation.
---

# 产品档案（指路）

对照十五节清单深读台账里的产品上下文，只写覆盖索引与缺口。不在本仓库另建一份产品档案。

## 步骤

1. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）。把 `~` 展开为用户主目录，不要把 `~` 当相对路径。本会话还没读过就现在读。完成：能指出受众、品类、差异化各依据该文件哪几条；原文不拷进本仓库。
2. **参数**。规格、认证、容量等仍缺时，再读 `~/Documents/New/fact-base/` 里对应该品类的文件。不需要则跳过。完成：仍缺的参数标「未在上下文出现」，不编造。
3. **覆盖**。用「默认」十五节对已读材料打 有/缺。公开信息尚未能判定时，用网页搜索查证；需要原文则抓取指定 URL；搜索不可用则停止并写缺口，不编造。需要隔离时 dispatch a subagent, else do it inline。已经在上下文里的不要再问用户。完成：15 节都有状态。
4. **确认**。把覆盖判断（有/缺，不贴原文）交给用户过一眼，至少覆盖业务概览、ICP、差异化、证据点。完成：用户确认或列出要改的节。
5. **落盘** `deliverables/marketing/01-foundation/product-profile-index.md`，用下方模板。完成：文件非空；无产品原文、无证据库、无定位表；教学支架原文零出现。

## 默认

产品事实只读，不在本仓库另存。索引只写有/缺与路径。

覆盖这十五节（只打勾，不把正文抄过来）：

1. 业务概览 — 名称、产地、成立年、模式（OEM/ODM/批发）、品类、一句价值主张
2. 产品规格 — 材质或组件与变体、尺寸容量、MOQ、交期、认证、包装运输
3. 价值链 — 上游、中游直接客户、下游终端
4. 目标市场 — 主市场、扩展市场、进入渠道（以产品上下文为准）
5. ICP — 客户类型优先级、决策人/指定人/采购人、规模信号
6. 买家角色 — 3–5 个；role、行业、规模、目标、痛点、决策标准、发现渠道
7. 问题与痛点 — 核心问题、替代方案为何不够、业务代价
8. 竞争格局 — 具名直接对手及来源、替代方案、进口与本地动态
9. 差异化 — 已核实卖点、自有 vs 外协、客户选择理由
10. 异议与回应 — 常见异议、回应策略、至少两类不适合的客户
11. 客户用语 — 买家原话、行业术语、避免用词
12. 品牌语气 — 语气、沟通风格、语言规则
13. 贸易与出口 — 目标渠道、付款、运输条款、认证
14. 证据点 — 项目案例、产能、质量证据、评价、履历
15. 目标与指标 — 业务目标、关键转化动作、已知指标、增长目标

## 写法

- ICP 是客户类型；买家角色是决策人。分开打勾。
- 数字、证书、案例：上下文有才算「有」。空泛的 quality / service 不算有。
- B2B 直说，不把工厂或贸易做成 SaaS 口吻。
- 价值链三个层级都要有判定，不能只写「有客户」。

## 产出

```markdown
# 产品上下文覆盖索引

- source: 台账 product_context（不粘贴原文）
- fact_base: 读过 / 未需要
- confirmed: 是 / 否

## 覆盖

| 节 | 状态 | 指针 |
| --- | --- | --- |
| 业务概览 | 有 / 缺 | 路径或「未在上下文出现」 |

（十五节各一行）

## 缺口

- 节名：未在上下文出现
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是产品档案索引，例子教缺口形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

上下文有规格、没有产能。索引写成「规格：见 product_context；产能：未在上下文出现」，不要把规格表粘进交付物。

## 易错

- 把 ICP 和买家角色写成同一段，下游文案打不准决策人。
- 只读官网，忽略目标渠道店面、展会名录、第三方评价。
- 规格用非行业用语或生硬译文，后续 SEO 与广告会跟着错。
- 漏打贸易条款（付款、运输、认证）。
- 对手只写「同行厂家」，不看替代方案与进口/本地。
- 缺数时填价格、产能或交期。
- 把证据库、定位表或十五节正文写进本仓库，造成第二真相源。
- 跳过用户确认，直接进内容或广告。

## 清单

- [ ] 读过 `product_context`（缺参数才读 `fact-base/`），原文未拷进本仓库
- [ ] 十五节均有 有/缺；缺的未编造
- [ ] 用户已确认业务概览、ICP、差异化、证据点四项覆盖
- [ ] 文件在 `deliverables/marketing/01-foundation/product-profile-index.md`
- [ ] 交付物无产品原文、无证据库、无定位表；例子原文未进入交付物
