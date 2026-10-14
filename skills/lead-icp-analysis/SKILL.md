---
name: lead-icp-analysis
description: >
  Use when analyzing ICP, customer profile, buyer persona, target customer,
  ideal customer, customer segmentation, 客户画像, 目标客户, 理想客户,
  采购痛点, 销售策略, or B2B customer analysis, including phase 1 of this
  repo's lead run; or when the user asks for per-segment sales strategies
  before outreach. Segment buyers by industry vertical, trace buyer and
  sourcing-manager pain points to sources, and write a customized outreach,
  relationship, objection, and value strategy per profile. Read the ledger
  product_context (default ~/Documents/New/CONTEXT.md). Invent no market
  sizes or pain statistics. Not for company lists, contact scraping, cold
  emails, product positioning documents, or phase navigation.
---

# 客户画像分析（ICP）

按行业垂直切开理想客户画像，给每条 ICP 写可执行销售策略，落到 `deliverables/lead/01-icp/`。三条 Guidelines 的判定与查询模板见 `references/three-guidelines.md`。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录）。本会话还没读过就现在读。原文不拷进本仓库。核心只要两项就能开写：产品和目标市场。存在则再读 `deliverables/lead/00-system/interview-lead-icp-analysis.md` 当作已确认输入。存在 `deliverables/marketing/01-foundation/product-positioning.md` 则读其客群，作步骤 2 切开起点，不重切已确认客群。仍缺核心两项：先看用户本轮消息；仍缺则停并只要这两项。需要结构化补问时打开 `skills/lead-interview/SKILL.md` 并按其步骤做，不要在本文件另写问卷。完成：能指出产品与目标市场各依据哪几条；缺项标「未在上下文出现」。

2. **切开品类**。对照 `references/three-guidelines.md` 的 Guideline 1，按行业垂直与价值链位置提出候选 ICP。Guideline 1 的价值链位置列举仅为举例，不是默认五条；按产品上下文取舍，不要把教学例子里的行业名单当作默认名单。维度：行业类型、公司规模、市场细分、地理、采购频率。上限 5 条。产品上下文或访谈已排除的不列入。完成：短名单每条有价值链位置、与产品的关系、拟查证查询。

3. **查证**。对每条候选做三类查证：行业存在性、采购痛点、决策人结构。默认用网页搜索查证；关键判断再抓取指定 URL 的正文。查询年份用环境当前公历年。此时还没有目标公司，不按人名搜联系人。多条 ICP 需要隔离时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口，不编造。无相关结果的候选标 unverified，不进主名单。完成：主名单每条有可打开的来源；每次查询写入搜索日志。

4. **深描**。对主名单每条写 Overview、痛点、决策人。痛点必须行业特定、接到采购决策，并能指回来源 URL 或摘录。决策人写采购行为（频率、批量、渠道偏好）、决策标准（价格 / 质量 / 交期 / 证书 / 关系的相对权重）、个人痛点（KPI、压力、信息渠道）。规模、金额、趋势：来源有才写，并带来源与年份。完成：每条主名单 ICP 三块齐全；「在意质量与价格」这类空泛痛点为零。

5. **按 ICP 写策略**。对照 Guideline 2，每条写四维，且必须直接回应该条痛点：Outreach（首触渠道 + 具体说法）、Value Proposition（对该画像强调的卖点；竞争对比句以 `lead-usp-extraction` 稿为准，本 skill 不提前写外发主句）、Objection Handling（最常见异议 + 反驳）、Relationship Building（从首触到信任）。只使用产品上下文已有的能力、证书与案例；未持有的不得写成动作。推荐展会前须用网页搜索核对该展会对应该利基与区域。换名测试：把 ICP 名称换掉后策略仍成立 → 重写。完成：四维齐全；换名即垮。

6. **总体策略并落盘**。写 Overall Sales Strategy：跨画像的核心打法、资源优先级（先做哪条、为什么）、差异化定位摘要（引用 `deliverables/marketing/01-foundation/product-positioning.md`，不重写定位；无定位稿则标缺口，不另起定位句）。每条标 P0 / P1 / P2。按下方模板写入 `deliverables/lead/01-icp/icp-analysis.md` 与 `deliverables/lead/01-icp/icp-summary.xlsx`（当前环境写不了 xlsx 则同目录写 `icp-summary.csv`，列相同，并在 Markdown 注明）。完成：主报告非空；表列名匹配；教学例子原文零出现。

7. **出门检查**。对照清单与 `references/three-guidelines.md` 的判定。主名单目标 3–5 条，上限 5。低于 3：按实有条数交付并写缺口，不编第三条。进入主名单的 ICP，痛点与行业判断目标每条 ≥3 个独立来源（行业报告、论坛、贸易数据）；凑不到则该条标 unverified 或不入主名单，不拿软文凑数。完成：清单可逐条勾选。

## 默认

- 本 skill 无硬依赖，是获客 phase 1 入口。下游（搜索词、公司名单、联系人、竞品、USP、外展）见 `skills/lead-generation/SKILL.md`，不在本文件另写管线。已有 `deliverables/marketing/01-foundation/product-positioning.md` 客群则作切开起点，不重切；「差异化定位摘要」引用定位稿、不重写定位。产品定位走 `marketing-positioning`。
- 查证用网页搜索；需要原文时抓取指定 URL。概念型最低查证见 `skills/lead-generation/references/search-protocol.md`；实际次数写入搜索日志。达不到不编造、不空搜凑数。
- 策略与分析用中文；表列名 English snake_case；公司名与 ICP 英文名不翻译。
- 数字必须能回溯产品上下文或已抓取 URL。缺来源写缺口。
- 进度只认台账。产出只进 `deliverables/lead/01-icp/`。不要建仓外产出根。
- 单文件、无并行机会的工作 inline 做完。

## 写法

- 写他们需要什么，而不是他们是什么。
- 每条策略必须能直接用于后续冷邮件个性化；首触不要停在渠道名。
- 采购习惯按目标区域写，不把单一市场的习惯套到所有区域。
- B2B 采购行为与 B2C 消费行为分开。
- 「价格敏感」不得作为每条 ICP 的万能痛点。
- 深度优先于条数。

## 产出

主文件 `deliverables/lead/01-icp/icp-analysis.md`。表 `deliverables/lead/01-icp/icp-summary.xlsx`（或 `.csv`）。

```markdown
# ICP Analysis — {品类} × {市场}

- source: 台账 product_context（不粘贴原文）
- market:
- accessed:
- icp_count:

## 客户画像

### 1. {中文名}（{English Name}）

#### Overview
- 这些公司做什么
- 在供应链中的位置
- 与产品的关系
- company_size / geographic_focus（有来源才写）

#### 痛点分析
- Pain point 1: 〔具体，接到采购决策，带来源〕
- buying_criteria
- decision_makers（职位、行为、标准、个人 KPI）

#### 销售策略
- **Outreach**:
- **Value Proposition**:
- **Objection Handling**:
- **Relationship Building**:
- priority: P0 / P1 / P2

## Overall Sales Strategy

- 跨画像核心打法
- 资源优先级（先谁、为什么）
- 差异化定位摘要（引用定位稿，不重写）

## 搜索日志
| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|
```

表列：`icp_name, industry, company_size, geographic_focus, pain_points, buying_criteria, decision_makers, outreach_strategy, value_proposition, objection_handling, priority`

审查要的「销售策略」由各 ICP 的销售策略小节覆盖。Relationship Building 写在 Markdown；表沿用上列，不另加列。

## 例子

> 仅供理解，禁止引用到输出。

痛点接到采购决策才算数：不要写「在意质量和价格」。形状借自买家人格调研的栏目（是谁、钱怎么赚、谁拍板、双闸、中间带），不是某品类结论。

输入写「安装商」一条 → 成稿应拆名册闸与完工闸，不要写成统一执照。输入写「工商业客户」→ 成稿应标对大户太小、对门店太大的中间带，不要只用容量口号当画像名。输入把规划与采购合成一条 → 成稿应写商务闸与技术闸，后者可否决前者。自己是分销层时，二阶转售商不进客户名单。块形状与换名测试见 `references/examples.md`。

## 易错

- 未读产品上下文就开写，或把档案原文拷进本仓库。
- 用模型记忆填市场规模或痛点统计。
- 五条策略只换了 ICP 名称。
- 把 Guideline 1 或教学例子里的行业名单当作默认 ICP。
- 未持有的证书或未核对的展会写成动作。
- 在还没有目标公司时搜联系人。
- 为凑 3 条或凑搜索次数而编造。
- 把 skill 例子原文写入交付物。
- 本文件另写一套获客阶段。

## 清单

- [ ] 已读 `product_context`；产品与目标市场可回溯
- [ ] 主名单每条含 Overview、痛点、决策人、四维策略
- [ ] 痛点行业特定且有来源；策略换名即垮
- [ ] Overall Sales Strategy 有优先级；差异化定位摘要引用定位稿、未重写定位
- [ ] 表列名匹配；主报告含客户画像 / 痛点分析 / 销售策略 / Overall Sales Strategy
- [ ] 搜索日志有 URL 与日期；无编造数字
- [ ] 例子原文未进入交付物
- [ ] 文件在 `deliverables/lead/01-icp/`
