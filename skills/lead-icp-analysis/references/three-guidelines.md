# 三条 Guidelines（判定与查询）

条件：切开品类、深描、写策略或做出门检查时读本文。执行顺序与完成条件以 `SKILL.md` 为准。

## 目录

- [Guideline 1 客户画像](#guideline-1-客户画像)
- [Guideline 2 销售策略](#guideline-2-销售策略)
- [Guideline 3 数据与逻辑](#guideline-3-数据与逻辑)
- [查询模板](#查询模板)
- [判定](#判定)

## Guideline 1 客户画像

按行业垂直切开，再深描，再标决策人。常见价值链位置按产品上下文取舍，不默认全写：OEM、MRO、分销商、维修公司、终端行业用户。

**切开维度（每条候选都要能填）：** 行业类型、公司规模、市场细分、地理、采购频率。

**深描：** 先写这类公司做什么、在供应链哪一环、与产品的关系；再写痛点、需求、挑战。痛点必须该行业特有。

**决策人：** 买家与 sourcing manager。每条写齐：

- 采购行为 — 频率、批量、渠道偏好
- 决策标准 — 价格 / 质量 / 交期 / 证书 / 关系的相对权重（不要五条画像写成同一排序）
- 个人痛点 — 被考核的 KPI、压力、常用信息渠道

## Guideline 2 销售策略

每条 ICP 单独写策略，直接回应该条痛点，禁止跨画像套模板。四维与 `SKILL.md` 产出模板字段对齐（名称以产出模板为准）：

| 维 | 必须写到的粒度 |
| --- | --- |
| Outreach | 首触渠道 + 具体说法与步骤，不只渠道名 |
| Value Proposition | 对该画像强调哪几个卖点，且卖点来自产品上下文 |
| Objection Handling | 该画像最常见异议 + 对应反驳 |
| Relationship Building | 从首触到信任的具体动作 |

推荐展会：先用 Apify 搜索核对该展会与利基、区域相关，再写入 Outreach。未持有的证书、样品计划、案例不得写成已有动作。

## Guideline 3 数据与逻辑

- 行业判断、痛点、规模数字必须能回溯到本轮搜索或已抓取正文，不写无出处的「普遍认为」。
- 洞察按目标区域的贸易与制造采购逻辑写，领域（目标行业、痛点）要与出口销售相关。
- 主名单每条目标 ≥3 个独立来源（行业报告、论坛、贸易数据）。凑不到 3 个：该条标 unverified 或不入主名单，不拿内容农场或目录站凑数。
- Apify 修复与替代取证后仍不可得相关结果的候选标 unverified，不用训练记忆补成一条 ICP。已核验 3 条优于掺了 2 条编造的 5 条。

## 查询模板

花括号是字段，取产品上下文与候选 ICP，不是要抄进交付物的句子。`{year}` 用环境当前公历年。

行业存在性：

```
"{industry}" market size {target_market} {year}
```

采购痛点：

```
"{industry}" procurement challenges
"{industry}" pain points supply chain
B2B buyers of {product_category} procurement decision process
```

决策人结构（只查典型职位与部门，不搜具体人名）：

```
"{industry}" company purchasing department structure
"{industry}" buyer job title procurement manager
```

策略落地：

```
B2B sales strategy "{industry}" "{product_category}"
```

需要论坛或报告原文时，抓取指定 URL 的正文。职业网络按人名搜联系人此时过早。

## 判定

- **痛点：** 能改写为「该类买家因为〔来源中的具体机制〕而在〔采购决策〕上卡住」，并附 URL 或摘录。不能改写的删掉。
- **换名：** 把 ICP 英文名换成另一条后，Outreach / Value Proposition / Objection Handling / Relationship Building 仍通顺 → 该策略失败，重写。
- **条数：** 上限 5。目标 3–5 条已核验。低于 3 按实有交付并写缺口，不编第三条。
- **区域：** 北美、欧洲、中东等地采购习惯不同；只写本轮目标市场，并标出所依据来源。
