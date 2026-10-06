# 获客依赖图

编排器做闸门检查时读本文件。阶段目录小写；方法 skill 在 `skills/<name>/SKILL.md`；战役产出在 `deliverables/lead/<阶段>/`。

## 目录

- [横切](#横切)
- [阶段](#阶段)
- [技能登记](#技能登记)
- [依赖边](#依赖边)
- [状态判定](#状态判定)
- [闸门](#闸门)
- [预期产出与审查清单](#预期产出与审查清单)
- [中文名](#中文名)
- [机器可读图](#机器可读图)

## 横切

- 每个方法 skill 依赖台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`）。读不到则停，打开 `skills/marketing-profile/SKILL.md` 与 `skills/marketing-product-profile/SKILL.md`（文件存在时）。
- 共用规则：`skills/marketing-playbook-standards/SKILL.md`（存在则读）。
- 台账或 `deliverables/lead/` 缺失：打开 `skills/marketing-init/SKILL.md`。
- 教学产出进 `deliverables/lead/00-system/`，不占用战役 phase。
- 方法 skill 文件不存在 → 该节点不可跑，编排器停并写缺口。
- `lead-company-research` 的 emerging 产出、`lead-distributor-research` 的 brief 产出是同一 skill 的第二种交付物，不是另一个入口。

## 阶段

| 阶段目录 | 方法 skill |
| --- | --- |
| （phase 0，无目录） | 只读产品上下文 |
| `00-system` | `lead-teach`（元产出） |
| `01-icp` | `lead-icp-analysis`、`lead-search-term-expansion` |
| `02-companies` | `lead-company-research`、`lead-distributor-research`、`lead-retailer-research` |
| `03-contacts` | `lead-contact-discovery` |
| `04-market` | `lead-competitor-analysis`、`lead-market-analysis` |
| `05-usp` | `lead-usp-extraction`、`lead-product-knowledge` |
| `06-outreach` | `lead-cold-email-gen`、`lead-warm-email-transform`、`lead-followup-sequence`、`lead-email-sequence-strategy`、`lead-magnet-gen` |
| `07-targeted` | `lead-targeted-research`、`lead-targeted-outreach` |
| `08-linkedin` | `lead-linkedin-topic-research` 及各 `lead-linkedin-*` 帖类型 |
| `09-seo` | `lead-seo-editorial-guidelines`、`lead-seo-outline-gen`、`lead-seo-content-gen`、`lead-seo-content-edit` |
| `10-sales` | `lead-service-first-contact`、`lead-service-quotation`、`lead-service-objection`、`lead-service-first-order`、`lead-service-delivery`、`lead-service-retention`、`lead-buyer-psychology` |
| `99-archive` | 归档，不跑方法 |

## 技能登记

路径均为本仓库相对路径。表文件与策略文档同目录。

| Skill | 策略文档 | 表 |
| --- | --- | --- |
| `lead-icp-analysis` | `deliverables/lead/01-icp/icp-analysis.md` | `icp-summary.xlsx` |
| `lead-search-term-expansion` | — | `deliverables/lead/01-icp/icp-terms.xlsx` |
| `lead-company-research` | `deliverables/lead/02-companies/target-companies.md` | `target-companies.xlsx` |
| `lead-company-research`（emerging） | `deliverables/lead/02-companies/emerging-companies.md` | `emerging-companies.xlsx` |
| `lead-distributor-research` | `deliverables/lead/02-companies/distributors-analysis.md` | `distributors.xlsx` |
| `lead-distributor-research`（brief） | — | `deliverables/lead/02-companies/distributors-brief.xlsx` |
| `lead-retailer-research` | — | `deliverables/lead/02-companies/retailers.xlsx` |
| `lead-contact-discovery` | `deliverables/lead/03-contacts/collection-report.md` | `contacts.xlsx`；辅助 `domains-for-contact-finder.csv` |
| `lead-competitor-analysis` | `deliverables/lead/04-market/competitor-positioning.md` | `competitor-comparison.xlsx` |
| `lead-market-analysis` | `deliverables/lead/04-market/market-analysis.md` | `market-data.xlsx` |
| `lead-usp-extraction` | `deliverables/lead/05-usp/usp-strategy.md` | `usp-matrix.xlsx` |
| `lead-product-knowledge` | `deliverables/lead/05-usp/product-knowledge.md` | — |
| `lead-cold-email-gen` | `deliverables/lead/06-outreach/cold-emails.md` | — |
| `lead-warm-email-transform` | `deliverables/lead/06-outreach/warm-emails.md` | — |
| `lead-followup-sequence` | `deliverables/lead/06-outreach/followup-sequence.md` | — |
| `lead-email-sequence-strategy` | `deliverables/lead/06-outreach/email-strategy.md` | — |
| `lead-magnet-gen` | `deliverables/lead/06-outreach/lead-magnet.md` | — |
| `lead-targeted-research` | `deliverables/lead/07-targeted/research.md` | — |
| `lead-targeted-outreach` | `deliverables/lead/07-targeted/outreach.md` | — |
| `lead-linkedin-topic-research` | `deliverables/lead/08-linkedin/topic-research.md` | — |
| `lead-linkedin-authority` | `deliverables/lead/08-linkedin/authority-post.md` | — |
| `lead-linkedin-education` | `deliverables/lead/08-linkedin/education-post.md` | — |
| `lead-linkedin-mythbust` | `deliverables/lead/08-linkedin/mythbust-post.md` | — |
| `lead-linkedin-buyer-concern` | `deliverables/lead/08-linkedin/buyer-concern-post.md` | — |
| `lead-linkedin-market-challenge` | `deliverables/lead/08-linkedin/market-challenge-post.md` | — |
| `lead-linkedin-pain-solution` | `deliverables/lead/08-linkedin/pain-solution-post.md` | — |
| `lead-linkedin-behind-scenes` | `deliverables/lead/08-linkedin/behind-scenes-post.md` | — |
| `lead-linkedin-expertise` | `deliverables/lead/08-linkedin/expertise-post.md` | — |
| `lead-linkedin-faq` | `deliverables/lead/08-linkedin/faq-post.md` | — |
| `lead-linkedin-personal-story` | `deliverables/lead/08-linkedin/personal-story-post.md` | — |
| `lead-seo-editorial-guidelines` | `deliverables/lead/09-seo/editorial-guidelines.md` | — |
| `lead-seo-outline-gen` | `deliverables/lead/09-seo/outline.md` | — |
| `lead-seo-content-gen` | `deliverables/lead/09-seo/content.md` | — |
| `lead-seo-content-edit` | `deliverables/lead/09-seo/edited-content.md` | — |
| `lead-service-first-contact` | `deliverables/lead/10-sales/first-contact.md` | — |
| `lead-service-quotation` | `deliverables/lead/10-sales/quotation-strategy.md` | — |
| `lead-service-objection` | `deliverables/lead/10-sales/objection-handling.md` | — |
| `lead-service-first-order` | `deliverables/lead/10-sales/first-order.md` | — |
| `lead-service-delivery` | `deliverables/lead/10-sales/delivery.md` | — |
| `lead-service-retention` | `deliverables/lead/10-sales/retention.md` | — |
| `lead-buyer-psychology` | `deliverables/lead/10-sales/buyer-psychology.md` | — |

评审报告：`deliverables/lead/<阶段>/review/<skill>-review.md`。

## 依赖边

### 硬依赖（必须 approved 或 approved_with_concerns，或台账 `user_waiver`）

```
lead-icp-analysis -> []
lead-search-term-expansion -> [lead-icp-analysis]
lead-company-research -> [lead-search-term-expansion]
lead-company-research/emerging -> [lead-company-research]
lead-distributor-research -> [lead-search-term-expansion]
lead-distributor-research/brief -> [lead-distributor-research]
lead-retailer-research -> [lead-search-term-expansion]
lead-contact-discovery -> [lead-icp-analysis, ANY(lead-company-research, lead-distributor-research, lead-retailer-research)]
lead-competitor-analysis -> [lead-icp-analysis]
lead-market-analysis -> [lead-competitor-analysis]
lead-usp-extraction -> [lead-icp-analysis, lead-competitor-analysis]
lead-product-knowledge -> [lead-icp-analysis]
lead-cold-email-gen -> [lead-icp-analysis, lead-usp-extraction]
lead-warm-email-transform -> [lead-cold-email-gen]
lead-followup-sequence -> [lead-cold-email-gen]
lead-email-sequence-strategy -> [lead-cold-email-gen, lead-followup-sequence]
lead-magnet-gen -> [lead-icp-analysis]
lead-targeted-research -> [lead-usp-extraction]
lead-targeted-outreach -> [lead-targeted-research]
lead-linkedin-topic-research -> [lead-icp-analysis]
lead-linkedin-authority -> [lead-linkedin-topic-research]
lead-linkedin-education -> [lead-icp-analysis]
lead-linkedin-mythbust -> [lead-icp-analysis]
lead-linkedin-buyer-concern -> [lead-icp-analysis]
lead-linkedin-market-challenge -> [lead-icp-analysis]
lead-linkedin-pain-solution -> [lead-icp-analysis]
lead-linkedin-behind-scenes -> []
lead-linkedin-expertise -> [lead-icp-analysis]
lead-linkedin-faq -> [lead-icp-analysis]
lead-linkedin-personal-story -> []
lead-seo-editorial-guidelines -> []
lead-seo-outline-gen -> [lead-seo-editorial-guidelines]
lead-seo-content-gen -> [lead-seo-outline-gen]
lead-seo-content-edit -> [lead-seo-content-gen]
lead-service-first-contact -> [lead-icp-analysis, lead-usp-extraction]
lead-service-quotation -> [lead-service-first-contact]
lead-service-objection -> [lead-service-quotation]
lead-service-first-order -> [lead-service-objection]
lead-service-delivery -> [lead-service-first-order]
lead-service-retention -> [lead-service-delivery]
lead-buyer-psychology -> []
```

无硬依赖的节点可并行；有硬依赖的必须串行。`ANY(...)` 表示括号内至少一个已批准。

### 软依赖（有则读，不阻塞）

```
lead-distributor-research ~> [lead-company-research]
lead-retailer-research ~> [lead-company-research]
lead-contact-discovery ~> [lead-company-research, lead-distributor-research, lead-retailer-research]
lead-competitor-analysis ~> [lead-company-research]
lead-market-analysis ~> [lead-company-research, lead-distributor-research, lead-retailer-research]
lead-usp-extraction ~> [lead-market-analysis]
lead-product-knowledge ~> [lead-usp-extraction, lead-competitor-analysis]
lead-cold-email-gen ~> [lead-product-knowledge, lead-competitor-analysis]
lead-warm-email-transform ~> [lead-product-knowledge]
lead-magnet-gen ~> [lead-usp-extraction, lead-product-knowledge]
lead-targeted-research ~> [lead-company-research, lead-competitor-analysis]
lead-linkedin-* ~> [lead-usp-extraction, lead-product-knowledge]
lead-linkedin-education ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-mythbust ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-buyer-concern ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-market-challenge ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-pain-solution ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-behind-scenes ~> [lead-usp-extraction, lead-product-knowledge]
lead-linkedin-expertise ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-linkedin-faq ~> [lead-usp-extraction, lead-product-knowledge, lead-linkedin-topic-research]
lead-seo-outline-gen ~> [lead-icp-analysis, lead-competitor-analysis]
lead-seo-content-gen ~> [lead-seo-editorial-guidelines]
lead-seo-content-edit ~> [lead-seo-editorial-guidelines, lead-seo-outline-gen]
lead-service-first-contact ~> [lead-competitor-analysis]
lead-service-quotation ~> [lead-icp-analysis]
lead-service-objection ~> [lead-service-first-contact, lead-icp-analysis]
lead-service-first-order ~> [lead-service-quotation, lead-service-first-contact]
lead-service-delivery ~> [lead-service-quotation]
lead-service-retention ~> [lead-service-first-order, lead-service-quotation]
lead-buyer-psychology ~> [lead-icp-analysis, lead-service-first-contact, lead-service-objection]
```

## 状态判定

- 文件产出：看 frontmatter `status`。`approved` 或 `approved_with_concerns` 算通过闸门。
- 仅有表、无 Markdown：表文件存在且非空 → `draft`，须补 companion `.md` 的 status 才算批准。
- 文件在但未批准 → `draft`。
- 文件不在 → `missing`。
- 方法 `SKILL.md` 不在 → 不可跑。

## 闸门

- 产品上下文：台账 `product_context` 可读，否则停。
- 硬依赖：上游已批准，或台账记录 `user_waiver`。
- 审查：六维审查已做，或显式 `user_waiver`。
- 产出：策略文档与表进 `deliverables/lead/<阶段>/`；评审进 `deliverables/lead/<阶段>/review/`；元产出进 `deliverables/lead/00-system/`；归档进 `deliverables/lead/99-archive/`；进度只写 `state/status.md`。

## 预期产出与审查清单

审查时逐条 ✅/❌。任一 ❌ 至少降为 CONCERN。

配额口径：本清单中「至少 N 行 / 至少 N 个」均为**目标**。方法 skill 已按「目标 + 缺口」口径改写：实有数量不足、且交付物写明了尝试与缺口的，按实有质量审查（缺口记 CONCERN）；为凑数编造的公司、联系人、数字、来源，一经发现直接 FAIL。

### lead-icp-analysis

- Markdown 必含：客户画像、痛点分析、销售策略、Overall Sales Strategy
- 表 `icp-summary.xlsx` 至少 3 行；列：`icp_name, industry, company_size, geographic_focus, pain_points, buying_criteria, decision_makers, outreach_strategy, value_proposition, objection_handling, priority`
- 检查：痛点具体到行业；不同 ICP 销售策略有差异；含 Outreach + Relationship-Building + Objection Handling + Value；每个 ICP 至少 3 个真实来源

### lead-search-term-expansion

- 表 `icp-terms.xlsx` 至少 10 行，按 ICP 分 sheet；列：`icp_category, company_type, positioning_term, tone, search_keyword, estimated_search_volume, use_case`
- 检查：术语经搜索验证为公司真实自我描述；覆盖 Professional / Casual / Cutting-edge / Traditional；关键词不是生造；每个 ICP 至少 10 个不同术语

### lead-company-research

- Markdown 必含：公司概览
- 表 `target-companies.xlsx` 至少 10 行；列：`company_name, domain, country, employee_count, industry, annual_purchase_estimate, buying_behavior, supplier_preferences, decision_makers, selection_criteria, icp_category, data_source, url_verified, notes`
- 每家必须 3 信息块：可访问域名、Buying Behavior（年采购量 + 供应商偏好）、Decision Process（参与者 + 标准 + 影响因素）
- 检查：优先新兴高增长而非只堆知名大企业；所有域名已抓取验证可达；facts-based，actionable

### lead-company-research（emerging）

- 表 `emerging-companies.xlsx` 至少 10 行；上表列 + `founded_year, growth_signals`
- 检查：员工数小于 200；排除知名大公司；不与 `target-companies.xlsx` 重复；`growth_signals` 有具体证据（融资、招聘、新产品、扩张）

### lead-distributor-research

- Markdown 必含：分销商概览、合作潜力分析、Top 3 建议
- 表 `distributors.xlsx` 至少 10 行
- 11 维：Company Overview / Target Audience / Revenue & Size / Geographic Coverage / Product Portfolio / Market Position / USP / Customer Satisfaction / Supply Chain / Partnership Potential（须有深度）/ Website & Contact
- 检查：无空白维度；`contact_info` 至少有官网联系方式；若方法要求员工数小于 200 则核对；所有域名已抓取验证

### lead-distributor-research（brief）

- 表 `distributors-brief.xlsx` 至少 10 行；列：`company_name, domain, years_in_business, market_position, primary_customers, niche_focus, data_source, url_verified`
- 检查：不与详细版重复；域名可访问；信息经查证

### lead-retailer-research

- 表 `retailers.xlsx` 至少 10 行；列：`company_name, domain, years_in_business, market_position, primary_customers, niche_focus, employee_count, data_source, url_verified`
- 检查：员工数小于 200；`market_position` 为 leader / emerging / niche / regional；`niche_focus` 具体

### lead-contact-discovery

- Markdown 必含：采集概况、查证统计、失败分析、数据隐私提醒
- 表 `contacts.xlsx` 每家至少 1 行，按 ICP 分 sheet；列：`company_name, domain, contact_name, job_title, email, phone, linkedin_url, icp_category, company_type, data_source, confidence, collected_date`
- 辅助：`domains-for-contact-finder.csv`（仅当用户将使用已配置的发现服务）
- 检查：按 ICP / 公司类型 / 职位分列；邮箱未配置发现服务则标「联系人待补」，不编造；`confidence` 合理；含 GDPR / CAN-SPAM 提醒

### lead-competitor-analysis

- Markdown 必含：竞品定位策略分析、市场定位空白分析、差异化建议
- 表两 sheet：竞品定位（至少 12 行：`positioning_strategy, company_name, domain, target_audience, key_selling_points, market_position, data_source`）；市场空白（至少 3 行：`gap_description, current_status, opportunity, recommended_action, priority`）
- 检查：每种定位 2 家代表公司；每家 Overview + Target Audience + Key Selling Points；域名可访问；空白至少 3 个；建议可执行

### lead-market-analysis

- Markdown 10 板块：Executive Summary、市场概览、竞争格局、消费者行为、趋势与机会、SWOT、风险分析、财务预测、建议、附录
- 表三 sheet：市场数据汇总（`metric, value, source, year, category, notes`）；SWOT 矩阵（`type, description, evidence, impact_level, data_source`）；风险矩阵（`risk_type, description, probability, impact, mitigation, data_source`）
- 检查：10 板块全覆盖；数据有 source + year；SWOT 每条有证据；CAGR 与规模至少两源交叉；建议含时间线与行动

### lead-usp-extraction

- Markdown 必含：微利基市场分析、竞品情报、竞品 USP 挖掘、Gap 矩阵、能力叠加、差异化方案、定位与内容、USP-ICP 匹配
- 表：竞品 USP 矩阵（至少 15 行）；USP 清单（至少 4 行：`usp_headline, usp_type, buyer_angle, proof, target_icp, competitive_frame, priority`）
- 检查：七步都有交付物；Gap 基于真实搜索；Top-3 方案有 Buyer Impact / Ease / Cost / Time / Imitation Barrier；定位语不超过 14 词；不同 ICP 有不同主 USP

### lead-product-knowledge

- Markdown 必含：TL;DR、Product 101、Manufacturing Flow、Benchmarks、Compliance、Cost Drivers、Pitch Playbook、Objections & Proof Plan
- 检查：KPI 完整；benchmark 与 compliance 有来源；不编造合规标准；Pitch 按买家类型差异化；文化适配反映目标地区；中英不是直译

### lead-seo-editorial-guidelines

- 必含：Editorial Guidelines、Tone、Reading Level、Avoid、Text Format、Tips、Guidelines 块
- 检查：Tone 最多 2 个且有对比；可读性目标明确；Avoid 覆盖方法 skill 列出的反模式；有可直接使用的 Guidelines 块

### lead-seo-outline-gen

- 必含：Article Outline、Target Keyword、Article Type、Title、Meta Description、Introduction、Main Sections、Conclusion、Semantic Keywords、Competitor Gap Analysis、Search Intent Coverage
- 检查：遵循选定模板；每个 H2 映射至少一个搜索意图；竞品差距至少 3 个空白；语义关键词按意图分组；含 FAQ

### lead-seo-content-gen

- 必含：Article Title、Introduction、Conclusion
- 检查：逐章节生成；遵循编辑规范；body 有 helpfulness 元素；Introduction 有钩子，Conclusion 有 CTA

### lead-seo-content-edit

- 必含：Edit Report、Edited Article
- 检查：方法 skill 的检查清单全部覆盖；连贯性改善；外链建议具体；编辑有理由

### lead-linkedin-topic-research

- 必含：话题列表、角度分析
- 检查：ICP-first；有搜索支撑；多种高互动角度；至少 8 个话题

### lead-linkedin-authority / education / mythbust / buyer-concern / market-challenge / pain-solution / behind-scenes / expertise / faq / personal-story

- 各帖必含：帖子正文、策略说明（education / mythbust / faq 等另含候选列表，behind-scenes 另含视觉素材说明）
- 共用检查：遵守 `linkedin-post-guidelines.md`；软广原则；无无来源统计
- 分项：权威帖趋势真实；教育帖 tip 可操作；揭谣帖 myth 真实存在；关切帖 empathy-first；挑战帖区域特定；痛点帖从买家视角；幕后帖有视觉描述；专业帖可验证；FAQ 真诚；故事帖教训由故事引出

### lead-service-first-contact

- 必含：Market Insight Hook、3-Sentence Message、Differentiation Tagline、Embedded Lock-In Tactic
- 检查：Hook 基于真实市场数据；打断「只要价格清单」开场；Lock-In 像服务不是陷阱；中英都自然

### lead-service-quotation

- 必含：Smart Pricing Structure、Embedded Value Offers、Trust Clause、Outcome Framing、Reorder Logic
- 检查：从买家 ROI 呈现；Value Offers 低成本高感知；Trust Clause 可验证；Reorder 是便利不是合同绑架

### lead-service-objection

- 必含：Top 3 Objection Responses、Trust Narrative、Value Reframe、Visual Asset Idea、Embedded Lock-In
- 检查：Acknowledge → Reframe → Prove → Pivot；转向价值/结果；Trust Narrative 含可回溯数字

### lead-service-first-order

- 必含：Onboarding Checklist、Welcome Message、Shared Folder Contents、Soft Lock-In Device、Switching Friction Hint
- 检查：清单覆盖订单到交付；Welcome 不像空模板；Shared Folder 有文件类型与更新频率

### lead-service-delivery

- 必含：Visual Timeline、Proof Assets、Packaging Risk Protocol、Weekly Update Templates、Reassurance Deliverable
- 检查：时间线分阶段且有天数；每阶段至少 2 个 Proof Assets；模板含个性化占位；Packaging 引用真实行业标准

### lead-service-retention

- 必含：3-Phase Retention Plan、Loyalty Ladder、Reorder Lock-In Tools、Surprise Moment、ROI Boost Mechanism
- 检查：覆盖发货后 / 30 天 / 90 天；Loyalty 至少 3 层递增；Reorder 创造便利；ROI 计算可回溯

### lead-buyer-psychology

- 必含：场景选择、买家视角、顶尖销售视角、推荐话术
- 检查：共情 + 策略都在；洞察具体；话术像人说的；展会场景含肢体语言建议

外展类（cold / warm / followup / sequence / magnet）与定向类：交付物非空、不是例子原文；未配置外发工具则只产文案不发送。具体字段以各方法 skill 为准。

## 中文名

| Skill | 中文 |
| --- | --- |
| lead-icp-analysis | 客户画像分析 |
| lead-search-term-expansion | 搜索词扩展 |
| lead-company-research | 目标公司搜索 |
| lead-distributor-research | 分销商调研 |
| lead-retailer-research | 零售商调研 |
| lead-contact-discovery | 联系人采集 |
| lead-competitor-analysis | 竞品分析 |
| lead-market-analysis | 市场分析 |
| lead-usp-extraction | USP 提炼与差异化定位 |
| lead-product-knowledge | 产品知识 |
| lead-cold-email-gen | 冷邮件生成 |
| lead-warm-email-transform | 暖邮件转化 |
| lead-followup-sequence | 跟进邮件序列 |
| lead-email-sequence-strategy | 邮件策略编排 |
| lead-magnet-gen | 引流素材生成 |
| lead-targeted-research | 定向客户调研 |
| lead-targeted-outreach | 定向客户开发 |
| lead-linkedin-topic-research | LinkedIn 话题研究 |
| lead-linkedin-authority | LinkedIn 权威帖 |
| lead-linkedin-education | LinkedIn 教育帖 |
| lead-linkedin-mythbust | LinkedIn 揭谣帖 |
| lead-linkedin-buyer-concern | LinkedIn 买家关切帖 |
| lead-linkedin-market-challenge | LinkedIn 市场挑战帖 |
| lead-linkedin-pain-solution | LinkedIn 痛点解决帖 |
| lead-linkedin-behind-scenes | LinkedIn 幕后帖 |
| lead-linkedin-expertise | LinkedIn 专业帖 |
| lead-linkedin-faq | LinkedIn FAQ 帖 |
| lead-linkedin-personal-story | LinkedIn 个人故事帖 |
| lead-seo-editorial-guidelines | SEO 编辑规范 |
| lead-seo-outline-gen | SEO 文章大纲 |
| lead-seo-content-gen | SEO 内容生成 |
| lead-seo-content-edit | SEO 内容编辑 |
| lead-service-first-contact | 首次联系策略 |
| lead-service-quotation | 报价策略 |
| lead-service-objection | 异议处理 |
| lead-service-first-order | 首单流程 |
| lead-service-delivery | 交付透明度 |
| lead-service-retention | 客户留存 |
| lead-buyer-psychology | 买家心理分析 |

## 机器可读图

```json
{
  "version": 1,
  "tree": "lead",
  "global_gates": {
    "product_context": {
      "ledger_key": "product_context",
      "default": "~/Documents/New/CONTEXT.md",
      "block_if_unreadable": true
    },
    "review": {
      "required": true,
      "pass_status": ["approved", "approved_with_concerns"],
      "waiver_field": "user_waiver"
    }
  },
  "output_policy": {
    "strategy_docs": "deliverables/lead/<phase>/",
    "tables": "deliverables/lead/<phase>/",
    "review_reports": "deliverables/lead/<phase>/review/",
    "system": "deliverables/lead/00-system/",
    "archive": "deliverables/lead/99-archive/",
    "progress": "state/status.md"
  },
  "phases": [
    {"id": "0", "name": "product-context", "phase_dir": null},
    {"id": "1", "name": "icp", "phase_dir": "01-icp", "skills": ["lead-icp-analysis", "lead-search-term-expansion"]},
    {"id": "2", "name": "companies", "phase_dir": "02-companies", "skills": ["lead-company-research", "lead-distributor-research", "lead-retailer-research"]},
    {"id": "3", "name": "contacts", "phase_dir": "03-contacts", "skills": ["lead-contact-discovery"]},
    {"id": "4", "name": "market", "phase_dir": "04-market", "skills": ["lead-competitor-analysis", "lead-market-analysis"]},
    {"id": "5", "name": "usp", "phase_dir": "05-usp", "skills": ["lead-usp-extraction", "lead-product-knowledge"]},
    {"id": "6", "name": "outreach", "phase_dir": "06-outreach", "skills": ["lead-cold-email-gen", "lead-warm-email-transform", "lead-followup-sequence", "lead-email-sequence-strategy", "lead-magnet-gen"]},
    {"id": "7", "name": "targeted", "phase_dir": "07-targeted", "skills": ["lead-targeted-research", "lead-targeted-outreach"]},
    {"id": "8", "name": "linkedin", "phase_dir": "08-linkedin", "skills": ["lead-linkedin-topic-research", "lead-linkedin-authority", "lead-linkedin-education", "lead-linkedin-mythbust", "lead-linkedin-buyer-concern", "lead-linkedin-market-challenge", "lead-linkedin-pain-solution", "lead-linkedin-behind-scenes", "lead-linkedin-expertise", "lead-linkedin-faq", "lead-linkedin-personal-story"]},
    {"id": "9", "name": "seo", "phase_dir": "09-seo", "skills": ["lead-seo-editorial-guidelines", "lead-seo-outline-gen", "lead-seo-content-gen", "lead-seo-content-edit"]},
    {"id": "10", "name": "sales", "phase_dir": "10-sales", "skills": ["lead-service-first-contact", "lead-service-quotation", "lead-service-objection", "lead-service-first-order", "lead-service-delivery", "lead-service-retention", "lead-buyer-psychology"]}
  ]
}
```
