# 内容策略方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、支柱、评分与表结构以本文为准。

## 目录

- [输入](#输入)
- [采集](#采集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

先读台账 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；需要参数再读同目录 `fact-base/`）。上游若已存在则读：

- `deliverables/marketing/01-foundation/` 定位、买家角色、差异化
- `deliverables/marketing/02-seo/seo-audit.md` 关键词优先级与技术约束
- 已有内容清单：博客、产品页、视频、案例、渠道表现

产品事实不写进 skill，不另写公司档案。品类、目标市场、产地只引用产品上下文对应字段，不在本文填值。

缺项列缺口后停。

## 采集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期：

1. 该品类 B2B 内容营销策略
2. 该品类买家问题与 FAQ
3. B2B 制造内容中能带来询盘的选题
4. 该品类与替代方案的对比检索
5. 目标市场该品类趋势（当前或下一自然年）
6. 该品类安装或使用指南
7. 该品类项目案例
8. 该品类 OEM / 定制流程
9. B2B 外贸制造内容日历
10. 目标市场采购该品类的路径与关注点

结果不够时再补：竞品站点地图与长文、思想领导力稿、买家问题综述。仍用同一条搜索能力，不换工具品牌。

### 视频、职业社交与视觉信号

仅当产品上下文列出对应频道时才采集；未列出则该项记缺口，不编造播放量或互动。

- 视频：安装、设计思路、制造过程。记下选题、钩子、评论里的买家问题。
- 职业社交：3–5 个竞品或行业领袖的近期公开帖。记下格式、选题、可观察的互动信号。
- 视觉社区：该品类设计与应用关键词。记下图案/场景、应用、可观察的互动。

### 最低数据量

进入分析前至少备齐；达不到的写入缺口，不降低后项装成已完成。

- **30** 篇竞品文章/博客：title、URL、字数、选题、来源
- **20** 条视频或社交帖分析：选题、可观察的播放/互动、要点（频道不在产品上下文则整项记缺口）
- **50** 条视觉趋势帖：图案/场景、应用、互动（同上）
- **15** 个内容缺口：竞品覆盖弱或缺失的选题
- 表现基准：已观察到的、能带动互动或询盘的格式与选题

多站点抓取需要隔离时 dispatch a subagent, else do it inline。

### 校验

- 每个缺口引用 ≥2 个来源，证明竞品缺失或覆盖弱
- 每个推荐选题映射到真实检索词或已观察的买家问题
- 禁止编造互动指标；只用观察到的数据
- 日历日期对齐已核官方源的展会、采购旺季或其他行业周期（周期名单以产品上下文为准）

## 分析

### 四支柱

策略建在 4 个支柱上，各对应漏斗角色：

| 支柱 | 角色 | 选题方向 |
| --- | --- | --- |
| Educational | 捕获研究型买家的检索需求 | 材料指南、规格对比、安装维护、合规标准 |
| Inspirational | 用可能性制造需求 | 项目展示、设计趋势、应用图库、前后对比 |
| Commercial | 支撑询盘与下单 | 产品目录页、应用页、案例、价格指南、对比页 |
| Trust-Building | 转化考虑期买家 | 工厂/履约参观、质检流程、认证、客户证言、团队介绍 |

日历中每个支柱至少 3 条。无资产支撑的支柱标缺口，不把空支柱写成已覆盖。

### 缺口记录

每个缺口写：

- 选题名与 target keyword
- 竞品覆盖（谁写过、写得怎样、URL）
- 我方覆盖（none / partial / exists）
- opportunity score（1–10）：检索需求 × 竞品弱 × 我方能力；因子无来源则该项标「公开源未找到」，禁止填假搜索量
- recommended format（指南、案例、对比、视频、信息图）
- 数据来源与 URL

### 选题集群

每个集群 = 1 个支柱页 + 4–8 个支持页，全部内链。

结构模板（路径与关键词用产品上下文的品类字段替换，不把本段原文写入交付物）：

- 品类枢纽 → 材料选项、表面/工艺选项、尺寸/定制、应用场景、安装
- 应用枢纽 → 商业项目、住宅项目、酒店项目、零售项目、项目案例
- 对比枢纽 → vs 替代方案 A / B / C、采购指南

每个集群必须写出支柱页路径、支持页列表、target keywords、内链关系。

### 角色映射

角色以产品上下文为准。上下文出现的角色必须覆盖；未出现的不要编造。下表是方法默认方向，不是客群清单：

| 角色方向 | 内容需求 | 偏好格式 |
| --- | --- | --- |
| 采购经理 | 规格、MOQ、交期、合规 | 产品页、规格表、案例 |
| 项目承包商 | 安装、耐久、项目实例 | 技术指南、案例、视频 |
| 建筑师 / 设计师 | 设计灵感、定制、标准 | 图库、趋势报告、规格表 |
| 区域经销商 | 需求数据、毛利、供货稳定 | 市场报告、产品目录、FAQ |
| 渠道/电商采购 | 照片、MOQ、运输、退货 | 产品页、对比、FAQ |
| 质量 / 合规 | 认证、检测、质检流程 | 履约参观、认证页、技术指南 |

### 选题评分

入日历前按下列权重打分；无来源的因子不得假装有数。

| 因子 | 权重 | 打分依据 |
| --- | --- | --- |
| Buyer Impact | 40% | 买家对话出现频率、订单价值潜力 |
| Content-Market Fit | 30% | 独特产线/工艺洞察、图/视频资产是否齐 |
| Search Potential | 20% | 月检索量、竞品排名弱（须有来源） |
| Resource Requirement | 10% | 制作投入、资产、审批时间 |

## 交付

根目录：`deliverables/marketing/03-content/`。

### 主文档

`content-strategy.md`，每条对外建议引用采集来源：

1. **内容诊断** — 竞品内容审计：谁覆盖什么、用什么格式、缺口。每条声明附 Phase 采集来源。
2. **支柱与选题集群** — 4 支柱 + 集群图，绑到产品上下文的品类能力。
3. **内容缺口** — ≥15 条，含 opportunity score、recommended format、target keyword、来源。
4. **渠道分发** — 哪种内容去哪个渠道。渠道名单以产品上下文为准；至少覆盖上下文中已出现的 4 个渠道，不足 4 个则写缺口。
5. **行动清单** — P0 必须 / P1 建议 / P2 可选，并指向执行附件。

每个推荐选题含：title、format、target keyword、buyer persona、funnel stage、source citation。

### 工作簿

复制 `templates/content-strategy.xlsx` 为 `content-strategy.xlsx`。禁止只交空模板。每行 `source` 非空。不能写表时改 `content-strategy.json`，三个数组对应下表，字段同列名。

| Sheet | 最少行 | 列 |
| --- | --- | --- |
| Content Calendar | 30 | publish_date, title, format, pillar, target_keyword, buyer_persona, funnel_stage, channel, priority, source |
| Topic Clusters | 5 | cluster_name, pillar_page, supporting_topics, target_keywords, competition, priority, source |
| Content Gap Analysis | 15 | topic, target_keyword, competitor_coverage, our_coverage, opportunity_score, recommended_format, source |

填写约束：

- `publish_date` 为日历日（ISO），禁止只写月份
- `format`：Blog / Video / Case Study / Infographic（或产品上下文允许的等价格式）
- `pillar`：Educational / Inspirational / Commercial / Trust-Building
- `funnel_stage`：Awareness / Consideration / Decision / Retention-Referral
- `priority`：P0 / P1 / P2
- Topic Clusters 每行 `supporting_topics` ≥4
- Content Gap Analysis 的 `opportunity_score` 在 1–10
- `source` 必须含可访问 URL，禁止只写能力名或 N/A

模板已有列名时以模板为准，并保证含 `source`。

### 执行附件（按需，同目录）

- `content-calendar.md` — 3 个月周历：publish_date、title、format、target_keyword、channel、priority
- `topic-clusters.md` — 集群图：支柱页、支持页、内链、target keywords
- `content-briefs.md` — 前 3–5 个 brief：title、outline、target keyword、competitor references、word count、source
- `channel-distribution-plan.md` — 分渠道格式适配与发布节奏；覆盖产品上下文中 ≥4 个渠道

## 反模式

1. 没有受众研究就推荐格式。
2. 只给空的行业博客建议，没有具体标题和关键词。
3. 跳过竞品内容分析。
4. 编造互动指标、搜索量或竞品 URL。
5. 用空泛营销套话代替具体选题、格式和买家价值。
6. 推荐团队无法产出的内容（无资产、无专业、无审批带宽）。
7. 任何交付物行的 `source` 为空。

## 质量闸门

- [ ] 每条内容推荐有关键词或买家问题支持，并引用采集来源 URL
- [ ] ≥5 家竞品有内容审计与 URL
- [ ] 内容日历有具体日期，且对齐已核验的展会或采购周期
- [ ] ≥15 个缺口含 opportunity score 与来源
- [ ] 终稿无未替换占位符
- [ ] 每行有带 URL 的 `source`
- [ ] 集群写出支柱页与支持页的内链
- [ ] 四个漏斗阶段均覆盖
- [ ] 策略绑到产品上下文的品类与目标市场，不锁单一 SKU 示例

## 可验证断言

交付物文末写 5–10 条。评审可用下列形状核对：

1. `content-strategy.md` 含 ≥5 家竞品内容审计，每条附 URL
2. Content Calendar ≥30 行，每行非空 `publish_date`、`target_keyword`、`source`
3. Topic Clusters ≥5 行，每行 ≥4 个 supporting topics
4. Content Gap Analysis ≥15 行，每行 opportunity_score 在 1–10
5. 终稿不存在未替换的 `{{...}}` 占位
6. 日历覆盖 Awareness / Consideration / Decision / Retention-Referral
7. 四个支柱在日历中均有 ≥3 条
8. 每个 content brief 含 title、outline、target keyword、competitor references、word count、source
9. `channel-distribution-plan.md` 覆盖 ≥4 个渠道（以产品上下文已出现者为准），并写明频率与格式
10. 引用 URL 抽查可访问；抽 20% 时成功比例应 ≥80%，否则把失败 URL 列入缺口
