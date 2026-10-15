---
name: lead-linkedin-market-challenge
description: >
  Use when market challenge, regional challenge, local market
  conditions, country-specific LinkedIn post, region-specific
  solutions, 市场挑战, 区域解决方案帖子, 特定市场帖子, or
  named-country constraints such as humidity, coastal corrosion,
  fire codes, winter, heat, or local building codes, including
  phase 8 LinkedIn of this repo's lead run. Research
  geography-specific climate, regulation, and standard obstacles,
  match them to evidenced capabilities, and write Structure 20
  posts under deliverables/lead/08-linkedin/. Distinct from
  lead-linkedin-pain-solution (universal pain) and
  lead-linkedin-buyer-concern (sourcing fears). Invent no local
  codes or capabilities. Not for topic research or phase
  navigation.
---

# 市场挑战帖（Structure 20）

针对单一国家或同一气候/法规带，用三步管线写出「该地挑战 → 可核验方案」的 LinkedIn 帖，落到 `deliverables/lead/08-linkedin/`。缺区域证据或能力证据则标缺口，不编造。本 skill 只产帖稿；用户自行发布或经用户已配置的工具发布。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。帖子篇幅、钩子、CTA、标签、四种风格升级、软广与出门清单读 `skills/lead-generation/references/linkedin-post-guidelines.md`，不把该文件抄进本 skill 或交付物。完成：能复述数据锚定、例子禁引用、产出根、工具写能力，以及本帖必须走 Structure 20。

2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：已批准的 `deliverables/lead/01-icp/icp-analysis.md`。软依赖存在则读：`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/05-usp/product-knowledge.md`、`deliverables/lead/08-linkedin/topic-research.md`。用户本轮给出的国家/地区、该地买家角色、已知挑战主题、证明材料、CTA 视为本轮输入，来源记「用户本轮」。硬依赖文件缺失、用户本轮也未给出该地+受众、且无 `user_waiver` → 停。目标地仍有多国候选、用户未点名时，列出候选并停，不写跨国混帖。区域或受众缺到无法下笔：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不在本文件另写问卷。完成：能指出**单一**目标地、该地受众、品类各依据哪几条；原文不拷进本仓库。

3. **查证并列出区域挑战（管线第 1 步）**。用网页搜索查证该地、该受众、该品类下的障碍；需要原文则抓取指定 URL。查询年份用环境当前公历年。三类意图都要覆盖：区域挑战、本地气候/基建/标准、公开市场上是否已有针对性改型（用来核对「此地真有此题」，不是用来抄竞品卖点）。花括号是字段，不抄进交付物：
   - `"{product_niche}" challenges {target_country} {year}`
   - `"{product_niche}" regulations requirements {target_country}`
   - `What specific challenges do {target_audience} face when sourcing {product_niche} for use in {target_country}?`
   - `"{target_country}" climate conditions infrastructure impact on {product_niche}`
   - `"{target_country}" {industry} standards requirements`
   - `"{product_niche}" adapted for {target_country} market`
   - `"{product_niche}" {target_country} market solutions`
   次数对齐 `skills/lead-generation/references/search-protocol.md` 的概念型最低要求；有用结果不够则报告实际次数与缺口，不空搜凑数。搜索不可用则停止并写缺口，不编造法规、气候或标准。多意图需隔离时 dispatch a subagent, else do it inline。每条挑战写「为何在此地成立」；做换国测试：把地名换成任意另一国仍成立 → 太泛，丢弃或标 `unverified`，不入主名单。法规或气候只覆盖一国时，目标必须是该国，不把该条扩成整个大区。目标 10 条互不重复的区域特定挑战；有证据的按实有条数写，不足 10 在缺口写明，禁止用任何市场都成立的贸易问题凑数。完成：主名单每条有 `why_here` 与 URL 或摘录；搜不到的标 `unverified` 且不入帖。

4. **针对性方案（管线第 2 步）**。入帖挑战优先：用户本轮点名且通过换国测试的 → 证据最强且产品上下文能对上的。对入帖的每一条，从产品上下文、USP、产品知识或用户本轮确认的能力里写 2–4 句方案，直接回答该条挑战。只检查上下文里真实存在的侧面：设计、工艺、材料、质检、测试、技术支持。禁止用「公司理应具备」补造工艺、材料、认证或该地项目。对不上则换一条；能对上的少于 1 条 → 只交付挑战表并停，不写面客方案段。用户点名多条则每条一篇，仍写入同一主文件。完成：入帖方案能指回 `capability_source`；买家收益写成该地买家能感到的结果，不是规格复读。

5. **按 Structure 20 起草并落盘（管线第 3 步）**。钩子必须点名该国/地区与该条挑战。正文五段按「写法」一次写齐，再写成可复制的整帖。标签 3–5 个且含 1 个区域标签，其余按共用规范。用户点名四种风格升级之一时，只改语气与结构，不改核心信息。对照共用规范出门清单后写入 `deliverables/lead/08-linkedin/market-challenge-post.md`。不代发布：`publish_status: copy_only`。过证据闸、审稿到 `operator_ok` 后由操作者亲手发，发完走执行登记（`skills/marketing-execution-log/SKILL.md`）。完成：主文件含挑战表、入帖方案、可复制英文帖、中文策略说明、来源与搜索日志；教学例子原文零出现。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批、不代替发布。

## 默认

- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存档案。
- 硬依赖是 ICP；软依赖（USP、产品知识、话题研究）有则读，不阻塞。话题研究只提供候选角度，不能把非区域话题改写成市场挑战帖。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。训练记忆不能充当当地法规、气候或标准的来源。
- 本帖处理**地理特定**障碍（气候、法规、本地标准、该地基建）。普遍运营痛点走 `skills/lead-linkedin-pain-solution/SKILL.md`（文件存在时）；供应关系顾虑走 `skills/lead-linkedin-buyer-concern/SKILL.md`（文件存在时）。全局趋势走 `skills/lead-linkedin-authority/SKILL.md`（文件存在时）。选题卡走 `skills/lead-linkedin-topic-research/SKILL.md`（文件存在时）；多平台日历或战役走 `skills/marketing-social-content/SKILL.md`（文件存在时）。本文件不写那些帖型。
- 进度只认台账。产出只进 `deliverables/lead/08-linkedin/`。Markdown only，不写表文件。
- 策略与缺口用本轮语言（缺省中文）；帖子正文与标签缺省英语，用户本轮点名其他面客语种再改；同一段不中英混排。
- 本 skill 只产帖稿，不经任何工具代发布；发帖一律由操作者亲手做。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。

## 写法

- Structure 20 骨架（顺序固定，五段都要有）：
  1. **Hook**：该地挑战 + 点名国家/地区；必须落在共用规范的折叠前。
  2. **Challenge context**：为何这是**此地**的问题，不是全球贸易套话。
  3. **Tailored solution**：产品/公司如何针对该挑战（有证明才写证明）。
  4. **Buyer benefit**：对该地买家意味着什么（当地项目、合规、气候或标准上的可感结果）。
  5. **CTA**：恰好一个，面向该地买家；句式见共用规范。
- 换国即垮：挑战、钩子、方案、收益任一把地名换掉仍成立 → 重写。
- 软广：产品句最多 1–2 句，去掉后帖子仍应独立有用。用经验口吻接到该地条件，不用规格清单。
- 上下文没有该地项目、年限或认证 → 不写「我们在该市场长期供货」。
- 空话（high quality、world-class、leading）无证据则删。无来源统计不写。
- 段落短、段间空行；专业、可核验、先把当地条件说清楚再给方案。

## 产出

主文件 `deliverables/lead/08-linkedin/market-challenge-post.md`。

```markdown
# Market Challenge Post

- source: 台账 product_context（不粘贴原文）
- accessed:
- target_country_or_region:
- target_audience:
- selected_challenge:
- selected_by: user | agent_recommended
- publish_status: copy_only（AI 不代发；发没发以执行登记为准）

## 挑战列表（目标 10）

| id | challenge | why_here | evidence_url | verified | capability_fit |

## 入帖方案

- challenge:
- solution:
- capability_source:
- buyer_benefit:

## Structure 20

**Hook:**
**Challenge context:**
**Tailored solution:**
**Buyer benefit:**
**CTA:**
**Hashtags:**

## 帖子（可复制）

[完整英文帖，可直接粘贴]

## 策略说明

## 来源

| 声明 | URL 或上游文件 | 访问日期 | 摘录 |

## 搜索日志

| 查询或 URL | 日期 | 结论 |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 挑战表目标 10 条；不足已在缺口写明；入帖那条通过换国测试且 `verified` 非空
- 方案能指回 `capability_source`；无能力则未写面客方案段
- 可复制帖含 Structure 20 五段；恰好一个 CTA；3–5 个标签且含区域标签
- 已对照 `skills/lead-generation/references/linkedin-post-guidelines.md`
- 含数字的句子有来源或已删除
- `publish_status` 必为 `copy_only`
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入写「欧洲市场并网很难」。这是大区套话，换国仍成立。应改成单一目标地的一条，形状对照「一国一闸 / 一国一卡点」：该地投运卡在配网商材料包或登记表，或该地电价把合同容量卡在尖峰窗口。行业里同一批发店（如 Memodo 这类多国店面）会把同一货架换成四个品类名、同一平台换成四套登记话术——钩子只点名其中一国与那一条，不要把四国闸口写成一篇跨国帖。中间功率段大厂不接、本地班组接不住，只在该地供给形状有证据时入表；公开目录+锁价是货架结构，有的市场公开标价，不要当地理挑战。不要把「目录批发交货后沉默」贴上国名交差，那是渠道定位不是地理障碍。方案只写上下文已有的能力，没有就标「未在上下文出现」。不要把一国配网规则或税口径扩成整个大区，不要把工况名本身当成地理挑战，不要把「运费高 / 缺证书」写进主名单，也不要把本节句子粘进交付物。

## 易错

- 没读 ICP 与产品上下文就发明当地法规或气候。
- 用任何市场都成立的贸易问题凑满 10 条。
- 把一国法规/气候写成整个大区的帖。
- 方案段写「理应能做」的改型，而不是上下文已有的能力。
- 把痛点帖或关系顾虑帖改贴一个地名交差。
- 无证据写该地项目经验或年限。
- 把教学例子或搜到的帖文原文写入交付物。
- AI 代发或代发布（不论是否配置工具、用户是否要求），或把成稿当成已发出。
- 终稿残留未解释的 `{{...}}`。
- 跳过查证，用训练记忆当当地标准。

## 清单

- [ ] 已读共用规则、帖子共用规范与 `product_context`；硬依赖已读或已停并写缺口
- [ ] 单一目标地；挑战表目标 10 条，入帖那条换国即垮且有来源
- [ ] 三类查证意图已覆盖；搜索日志非空；缺搜索已停并写缺口
- [ ] 方案能指回能力来源；无来源统计；无未持有的该地经验
- [ ] Structure 20 五段齐全；钩子点名国家/地区；恰好一个 CTA；3–5 个标签含区域标签
- [ ] 文件在 `deliverables/lead/08-linkedin/market-challenge-post.md`；未代发布
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
