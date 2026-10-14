---
name: marketing-copy-editing
description: >
  Use when copy edit, polish copy, review marketing copy, tone check,
  proofread, rewrite copy, copy polish, 文案编辑, 文案审查, 文案润色,
  文案审核, or 修改文案. Run seven sequential sweeps on existing B2B
  marketing copy for clarity, voice, buyer benefit, proof, specificity,
  emotion, and friction; write an audit report, a project style guide,
  and a copy-audit table under deliverables/marketing/03-content/copy-editing/.
  Read the ledger product_context first; invent no numbers or testimonials;
  never paste skill examples into the output. Not for drafting a new value
  proposition from scratch, technical SEO audits, SEO 成稿编辑
  (`lead-seo-content-edit`), competitor crawls, campaign plans, or
  phase navigation.
---

# 营销文案审查与精修

对已有 B2B 营销文案做七轮顺序审查，落到 `deliverables/marketing/03-content/copy-editing/`。只用产品上下文里的事实；缺证据标缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **输入**。读台账 `state/marketing-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。已有定位或竞品文件则读 `deliverables/marketing/01-foundation/` 下对应交付物；已有网站文案则读 `deliverables/marketing/03-content/`。待审原文来自用户本轮消息或上述交付物。完成：能指出受众、语气、规格、证据各依据哪几条；原文不拷进产品档案。产品上下文或待审原文缺失则停并写缺口。
3. **定人定段**。写下本篇的买家角色与漏斗阶段后再改字。角色从产品上下文取；上下文没有则在采购、承包、经销、指定人、批发里选最贴近的一档，并标明「角色未在上下文出现，暂用」。漏斗：访问 → 询盘 → 样品 → 报价 → 下单 → 复购。完成：角色与阶段各有一个取值。
4. **对标**。行业术语或语气需要对标时，用网页搜索查证；需要原文则抓取指定 URL 的正文。记下 URL、访问日期与摘录。搜索不可用则不对标、不编造竞品原文，在交付物写缺口；七轮审查仍可只基于产品上下文做。需要隔离时 dispatch a subagent, else do it inline。完成：至少 2 条外部来源，或已写明搜索缺口。
5. **七轮审查**。按「写法」顺序跑完 1–7 轮；每轮结束后回扫上一轮是否被改坏。多篇文案需要隔离时 dispatch a subagent, else do it inline。完成：每条问题有 sweep 编号、具体改法、优先级、角色、漏斗阶段、来源。
6. **落盘** 到 `deliverables/marketing/03-content/copy-editing/`，用「产出」模板写 `copy-audit.md`、`style-guide.md`、`copy-audit.xlsx`。完成：三文件非空；表行列达到下方断言；教学支架原文零出现。
7. **回扫**。改完再跑一轮全七 sweep。有新问题则修，自动修补不超过 3 轮。完成：一轮下来无新问题，或已记录 `user_waiver`。

## 默认

- 先读完全篇再动笔。局部改写不得切断上下文。
- 语气：直接、有把握、专业。不用 DTC 口语，不用注册/免费试用口吻。下一步用「要规格 / 要报价 / 要样品」。
- 数字、证书、案例、项目名、国别：产品上下文有才写。没有就写「未在上下文出现」，禁止补造。
- 技术词（材质等级、工艺、表面处理、认证、Incoterms）买家要看的，不删；名称与产品上下文逐字一致。
- 默认渠道与付款、检测、交期口径以产品上下文为准，不锁某一平台。
- 查证用网页搜索；需要原文时抓取指定 URL。不写工具 ID。
- 产出只进 `deliverables/marketing/03-content/copy-editing/`。台账若已写其他 `output_dir`，仍以本目录为准，除非用户本轮点名改路径。
- SEO 成稿编辑走 `lead-seo-content-edit`。本文件审营销树已有文案，不编获客 SEO 长文。

## 写法

七轮必须按序。后一轮改完，回扫前一轮。

**第 1 轮：清楚。** 读者能否一次看懂。查：绕口句、指代不清、未解释的行话、歧义。产品上下文里的材质、表面、认证缩写，对非技术买家要有一句解释，不假设对方知道。

**第 2 轮：语气。** 听起来是否同一张嘴。查：正式度跳变、品牌口吻不一致、情绪断裂、非母语别扭句。用产品上下文的品牌语气；制造/贸易文案保持直接，不改成消费品牌口吻。

**第 3 轮：所以呢。** 每句是否回答「关我什么事」。查：只报功能不报后果。利益桥按角色变：经销看毛利与供货稳；承包看按期到货；开发看耐久与投入产出。角色利益必须能回溯产品上下文，不编造痛点。

**第 4 轮：证明。** 每条断言有没有证据。查：无依据的最高级、空洞的社会证明、未挣来的权威。空的「全球客户信赖」要具名项目或市场；空的「行业领先」要认证。证据只来自产品上下文或已抓取 URL；缺则标「未在上下文出现」。

**第 5 轮：具体。** 是否具体到无法套到任意一家。空话改问产品上下文里的数；没有数就标缺口，不把空话留在终稿。

| 空话 | 向上下文要的 |
| --- | --- |
| 缩短交期 | 实际生产交期（工作日） |
| 众多客户 | 真实项目数与市场名 |
| 样品快 | 实际样品发出时间 |
| 高品质表面 | 材质等级、表面类型、公差 |
| 有竞争力的价格 | 单价区间与 Incoterms |

**第 6 轮：情绪。** 是否让对的人有感觉。查：平铺、纯理性、没有风险画面。B2B 项目买家的杠杆是风险下降与职业声誉。场景必须能回溯上下文，不编造事故。

**第 7 轮：零阻碍。** CTA 旁还有没有摩擦。查：未答异议、缺信任信号、下一步不清楚。B2B 降风险（不是「立即购买」）：样品政策、第三方检测选项、生产过程质检影像、可核验的安装清单、明确的定金结构、时限清楚的下一步（如「24 小时内回复详细报价」）。以上每一项：上下文有才写进建议，没有就列缺口，不虚构政策。

漏斗阶段 → 优先轮次：

| 漏斗 | 优先 |
| --- | --- |
| 访问 | 清楚、情绪 |
| 询盘 | 所以呢、证明 |
| 样品 | 具体、零阻碍 |
| 报价 | 零阻碍、证明 |
| 下单 | 零阻碍、具体 |
| 复购 | 语气、所以呢 |

**技术口径**

- 材质与规格写到产品上下文里的等级、标准或型号，不写泛称。
- 工艺、表面、后处理三者分开，不混用。
- 单位跟目标市场；只有上下文要求时才并列公制与英制。
- 出现价格必须带贸易术语：币种、单价、单位、Incoterms、港口均取产品上下文；缺一项标缺口，不报无条款价格。

**双语**

- 品类名一篇一译，全文锁定。
- 材质、表面、认证跨语言同一套词。
- 认证名与产品上下文实际持有的证书一致。

**空话替换**（终稿用右列形状，证据仍须来自上下文）：

| 不用 | 改成 |
| --- | --- |
| Cheap | 有依据的价格表述 / 成本有效 |
| Mass-produced | 产能或批量能力（有数才写） |
| Generic | 可定制 / 按单做 |
| We are the best | 带证据的具体断言 |
| World-class | 具体认证或可核验项目 |
| Best quality | 具体材质 / 表面 / 认证 |

## 产出

目录：`deliverables/marketing/03-content/copy-editing/`

每条审查输出形状：

1. 原文（引用、不改）
2. 问题（sweep 编号、类型、具体哪里不行）
3. 建议修改（用产品上下文真实数据；缺则「未在上下文出现」）
4. 优先级：High / Medium / Low
5. 来源（哪一轮、哪个角色、外部则完整 URL）

`copy-audit.md` 与 `style-guide.md` 顶部 YAML：`title`、`skill`（`marketing-copy-editing`）、`generated_at`、`version`。

`copy-audit.md` 每条含：原文、问题类型、sweep 编号、具体改法、优先级、persona、funnel_stage、source。

`style-guide.md` 必含：tone of voice、terminology rules、forbidden words（至少 5 组替换）、formatting rules、persona-specific guidance。

`copy-audit.xlsx` 可从 `templates/copy-audit.xlsx` 复制后填行（无脚本则按列手写，不另造构建器）：

- **Audit Items** 列：`original_copy`、`issue_type`、`sweep_number`、`specific_problem`、`suggested_fix`、`priority`、`persona`、`funnel_stage`、`source`
- **Style Rules** 列：`rule_name`、`rule_description`、`applies_to`、`example_violation`、`corrected_example`、`source`

断言（未满足则不算完成）：

- Audit Items、Style Rules 以 ≥10 行为目标；质量优先，不足不凑，差额写入缺口
- `sweep_number` 只取 1–7；`priority` 只取 High / Medium / Low
- 每个 sheet 的 `source` 无空值；外部来源用完整 URL
- 每条建议都有 persona 与 funnel_stage
- 审查中至少覆盖材质等级、表面、Incoterms 三类技术词中的一类
- 终稿无未解释占位符；教学支架原文零出现

```markdown
# 文案审查报告

- source: 台账 product_context（不粘贴原文）
- persona:
- funnel_stage:
- external_sources:

## 条目

### 1.

- original:
- sweep_number:
- issue_type:
- specific_problem:
- suggested_fix:
- priority:
- source:
```

## 例子

> 仅供理解，禁止引用到输出。

形状取自文案审计错误类型、术语 NEVER-SAY、重建硬规则（禁绝对化 / 禁选型 / Sibling Replacement）和跨境词表；只借结构，不写入型号、参数、价格或竞品原句。

输入：规格表已与产品上下文一致，营销段却另写一个数或换一套单位标签。审查应改散文对齐表格（sweep 1/4），或标「未在上下文出现」；不要把两个数揉成区间圆过去。

输入：把额定能力写成「规避某国并网规则、省一笔认证费」，或「无缝 / 不间断 / 零噪音 / 毫无折衷」。审查应删法规解读与绝对化（sweep 4）；可留能回溯上下文的场景收益。不要补官方没写的金额节省或家电负载清单。

输入：正文仍用上一代系列名或已换代的架构口头禅，或拿另一区域的认证/电压口径写本页。审查应改成上下文里的现行系列与标明区域（sweep 2/5），不要沿用旧名或把两套口径并列当卖点。

输入：兄弟页共用同一套利益句，或残留「请对照相邻档位确认本机」类占位。审查：家族共性可写但不得包装成本机独有；占位句删除，不填造出来的差异。出现「改选另一档」或贬抑同族，直接删，不换成另一条选型建议。

输入：「行业领先 / world-class / tier-1 / proven / 深受全球信赖」，或自造货架名（把贸易品类写成内部场次 / 第四解决方案）。审查应换成上下文里的具名项目、认证或该市场贸易品类名；没有证据就标缺口。不要用另一句光环词替换。

输入：自称「我们生产 / 我们的实验室 / 我们的质保 / 我们上门安装」。审查应改回产品上下文里的实际角色；不要用「我们不是中间商」来反向证明身份。

输入：把甲市场的认证专名堆进乙语言主标，或把并网写成另一市场的 utility 口头禅。审查应锁定目标市场用词（同一货架在不同市场用不同品类名）；不要为好懂而换制度。

输入 FAQ 问「该不该改订更大一档 / 这两台是不是同一台」。审查应删；改成挡住这一台下单的疑虑。不要补「适合哪类项目」的选型答。安装细则与上下文安装说明不一致时，改回上下文或标缺口，不要折中成更小的规格。

CTA 只保留上下文里有的下一步（要报价 / 要规格）；上下文没有样品政策就不要写申请样品。不用「立即购买」。

判决形状：与上下文一致可留；同页矛盾改散文；无依据标缺口；越界推导/选型/贬抑删除；填充模板删除；重复合并。不要为凑条数把已一致的句子再改一遍。

## 易错

- 没读完原文就局部改，上下文语义断裂。
- 套用 DTC 爆款规则，弱化 B2B 技术表达。
- 删掉买家要看的材质等级、认证、Incoterms。
- 为增强说服力编造案例、证书或份额。
- 把工艺、表面、后处理混为一谈。
- 引用外部对标或竞品语气却不写 source URL。
- 只列问题，不给可粘贴的改法。
- 终稿残留未解释占位符，或把本节例子原文写入交付物。
- 未对标时编造竞品原文或行业基准。

## 清单

- [ ] 已读共用规则与 `product_context`；待审原文在手
- [ ] 已写下 persona 与漏斗阶段
- [ ] 七轮按序做完，每轮后回扫
- [ ] 每条问题有具体改法、优先级、来源
- [ ] 技术口径与产品上下文一致；空话已替换或已标缺口
- [ ] 双语锁定（若双语言都在）
- [ ] 未编造证据；缺的写「未在上下文出现」
- [ ] CTA 是询价/规格/样品/验厂，不是立即购买
- [ ] `copy-audit.md`、`style-guide.md`、`copy-audit.xlsx` 已在 `deliverables/marketing/03-content/copy-editing/`
- [ ] Audit Items、Style Rules 以 ≥10 为目标，不足不凑并已写缺口；`source` 无空值
- [ ] 搜索可用则至少 2 条外部 URL；不可用则已写缺口
- [ ] 教学例子原文未进入交付物
