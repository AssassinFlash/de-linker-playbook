---
name: lead-product-knowledge
description: >
  Use when the user says product knowledge, product training, pitch
  playbook, objection handling, product 101, compliance matrix, 产品知识,
  产品培训, 话术手册, or 异议处理; when sales or training needs bilingual
  buyer-ready expertise from specs; or when preparing trade-show or
  sales-call materials. Read the fact-source entry docs/fact-sources.md; do not copy that archive into this repo.
  Classify the family, verify benchmarks and regional compliance, then
  write a sales or training report at brief, full, or deep_dive depth.
  Invent no certifications, tests, or numbers. Not for ICP interviews,
  USP extraction, competitor crawls, or phase navigation.
---

# 产品知识教练

把产品上下文里已有的规格，写成销售或培训能用的双语产品知识报告，落到 `deliverables/lead/05-usp/product-knowledge.md`。基准、合规与数字不编造。

## 步骤

1. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。本会话还没读过就现在读。原文不拷进本仓库。若存在则再读：`deliverables/lead/01-icp/icp-analysis.md`（按买家类型写话术的硬依赖）、`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/04-market/competitor-positioning.md`。规格、认证仍缺时按入口「什么问题查哪个源」再查。核心只要两项就能开写：产品和目标地区。其余（买家类型、规格/卖点、订单模式、销售障碍、用途/深度）用户给了再用，不追问齐全。缺核心两项：先看用户本轮消息；仍缺则停并只要这两项。需要结构化补问时打开 `skills/lead-interview/SKILL.md` 并按其步骤做，不要在本文件另写问卷。完成：能指出产品与目标地区各依据哪几条；缺项标「未在上下文出现」。

2. **模式**。用途 `sales`（对客、短、为成交）或 `training`（技术更深、教学口吻）；深度 `brief` / `full` / `deep_dive`。未指定则 `sales` + `full`。用户中途改模式：用已收集输入重渲，不再问一遍。完成：两种模式都写进交付物抬头。

3. **品类**。判定 `primary_family`；跨品类再给 `secondary_family`。读 `references/family-classifier.md`，加载该品类 KPI 与合规查证清单。对不上就新建品类，列 5–7 个 KPI 与合规需求。表内数字是分类先验，不是产品事实，禁止抄进报告。完成：品类名 + KPI 清单；混合品类写明主/次。

4. **查证**。用 Apify 搜索查证品类标准与 KPI、行业基准规格、目标地区进口合规与测试、成本结构、该类买家常见异议。需要原文时抓取指定 URL。Apify 修复与替代取证后仍不可得则停止并写缺口，不编造。需要隔离时 dispatch a subagent, else do it inline。每条基准与合规必须有 `source_hint`（URL，或「Unknown — verify via [测试/实验室/标准]」）。完成：每个目标地区都有合规行；无出处数字为零。

5. **撰写**。按深度渲染下方结构。双语：先英文，再一句能上场的中文，不要字对字直译。数字、证书、案例：上下文或本轮查证有才写。单位按目标地区（SI / imperial）。话术必须按「买家类型 × 地区」交叉，不能一套打天下。每个异议至少 2 条按说服力排序的证据；上下文没有的标「待补」，未持有的证书不得写成已有。完成：brief 含第 1、4、8、9 节；full 含 13 节；deep_dive 另加采购与工程附录；第 13 节必须在。

6. **落盘** `deliverables/lead/05-usp/product-knowledge.md`，用下方模板。只出 Markdown。完成：文件非空；抬头有用途×深度；教学支架原文零出现；未把产品档案原文整份粘进本仓库。

7. **出门检查**。对照清单。完成：品类与 KPI 匹配；基准皆有 `source_hint`；话术按类型有差异；口吻对得上目标地区；每个异议 ≥2 条排序证据；双语读得通；假设节诚实。

## 默认

**渐进披露**。先产品 + 地区；用户多给再用，不把选填当门禁。

**深度渲染**

- `brief` — 第 1、4、8、9 节
- `full` — 13 节全要
- `deep_dive` — 13 节 + 采购与工程附录

**地区口吻（话术与异议重点）**

- US — 直接、ROI、性能数字、性价比；异议常在价格辩护
- EU — 合规、可持续、质量来历、少浪费；异议常在合规与可持续证据
- ME — 关系、可靠、交期承诺；异议常在交期可靠性
- SEA — 灵活 MOQ、可改、快交期；异议常在付款条件

其他地区不要套用上表，按产品上下文与查证写，并标假设。

**上游**。ICP 文件缺失时，买家类型取产品上下文或标缺口，话术不得假装已个性化。USP / 竞品文件缺失则差异化锚点写「未在上游出现」。

## 写法

- 合规、测试、基准：查不到就写 Unknown，不要用模型记忆顶上。
- 话术连到该类买家的决策标准，不报功能清单。
- 中文用销售口吻，不用说明书直译。
- 用户已说的销售障碍必须进异议节。
- 上下文没有的认证可建议「待获取」，不得写成已有。
- 成本节必须落到可谈判杠杆，不停留在「材料贵」。
- 分类表、本 skill 例子、产品档案原文，都不是交付物素材。

## 产出

```markdown
# Product Knowledge Report — {Product} × {Region}

- source: 台账 product_context（不粘贴原文）
- purpose_mode: sales / training
- output_mode: brief / full / deep_dive
- primary_family:
- secondary_family: （无则无）

## 1. TL;DR Cheat Sheet (6-10 bullets)
通话速查表（关键要点）

## 2. Product 101 — Materials, Structure, Variants
产品基础——材料、结构、常见变体
（training 模式加 Sensory & Handling Notes）

## 3. Manufacturing Flow & QC Gates
生产流程与质量控制关口（分步，标注关键参数；参数须能回溯）

## 4. Industry Benchmarks & Typical Spec Ranges
行业基准与常见规格范围（每条 source_hint）

## 5. Compliance & Testing by Region
按地区的合规与测试（每条 source_hint；未知写 Unknown — verify via …）

## 6. Cost Drivers & Negotiable Levers
成本驱动因素与可谈判杠杆

## 7. Packaging, Labelling & Logistics
包装、标签与物流建议

## 8. Pitch Playbook by Buyer Type
按买家类型的话术手册（买家类型 × 地区）

## 9. Objections & Proof Plan
异议处理与证据呈现（每条异议 ≥2 条排序证据）

## 10. Smart Qualification Questions
资格审查提问清单

## 11. Red Flags & Risk Mitigation
红线与风控建议

## 12. Customization Menu & Rollout Roadmap
可定制选项与落地路线图

## 13. Assumptions & Unknowns to Confirm
假设与待确认信息

## 搜索日志
（查询意图、URL 或「Apify 修复与替代取证后仍不可得」、访问日期、摘录或缺口）
```

## 例子

> 仅供理解，禁止引用到输出。

只拿到品类和目标地区时，先写 brief：速查、合规缺口、通用话术，第 13 节列待补规格。不要空转等完整物料清单。资格问与异议按买家真问的分桶排：交易/账号、到货与到货损、保修找谁、现场症状、角色边界。店级采购、发货、退货、账号不写进第 2 节产品基础。

输入把第 8、9、10 节写成「电池」「质保」「物流」这类主题名。成稿改成症状或卡点问句（灯在闪、电量显示对不上、坏了找谁），答案是一线排查或路由，不是承诺。不要抄原厂或批发商原句，也不要把栏目名直接当问句。

分类表先验区间、竞品页数字、主张许可清单外的身份/时限/库存，都不得抄进第 4、5、8 节。上下文或本轮查证能指到的才写，带 `source_hint`；没有就「Unknown — verify via …」或「待补」。产品口径的问是装机前已经卡住的事（能不能配对、怎么接线、备电要不要另配箱子），同一档共用一套，不要逐型号写作文，也不要新种「是不是同一台」「哪个数才是上限」。

异议「坏了找谁」不要回成自有质保承保、备件库、或「去问厂家」。上下文有协调角色就写协调，有厂家条款就写条款出处；没有就标待补。不要把批发商热线或原厂时限数字抄进话术。异议「太贵」仍按说服力排序：第三方检测（仅当能指到）→ 批次不良率（仅当上下文有数字）→ 工厂 QC 录像（仅当有）；没有的标「待补」，不回「我们质量好」。

安装商要能上场说的开场，和 EPC 要进标书的合规来历，不要同一套第 8 节。美国分销商偏 ROI 与价格辩护，中东品牌方偏可靠；EU 偏合规与质量来历。库存、交期承诺、制造商身份都不当卖点。手册主语是干活的安装商或 EPC，不是户主；「你们装吗」进角色边界，不写进产品 101。交货即沉默的目录口吻改成工程伙伴口吻，但上下文没有的上门施工、调试执行、自有监控不得写成已有。

## 易错

- 没读产品上下文就写手册，或把档案原文整份粘进本仓库。
- 编造证书、测试结果、基准数字。
- 话术不随买家类型或地区变化。
- 中文字对字直译，上场说不出口。
- 只报功能，不连决策标准。
- 忽略用户已说的销售障碍。
- 把未持有的认证写成已有。
- 单位不看目标地区惯例。
- 成本节没有可谈判杠杆。
- 丢掉第 13 节，让用户拿不完整数据去谈。
- 把 `references/family-classifier.md` 的数字当已核实基准。
- 用具体搜索引擎名单代替「Apify 搜索查证 / 抓取指定 URL」。

## 清单

- [ ] 读过事实源入口 `docs/fact-sources.md` 并按其取证，原文未拷进本仓库
- [ ] 产品 + 目标地区已齐；模式已写进抬头
- [ ] 品类已判定；KPI 来自分类或新建，表内数字未抄进报告
- [ ] 基准与合规皆有 `source_hint` 或 Unknown；Apify 修复与替代取证后仍不可得已停并写缺口
- [ ] 深度对应的章节都在；话术按买家类型 × 地区有差异
- [ ] 每个异议 ≥2 条排序证据；未持有证书未写成已有
- [ ] 第 13 节诚实；双语可读
- [ ] 文件在 `deliverables/lead/05-usp/product-knowledge.md`
- [ ] 例子原文未进入交付物
