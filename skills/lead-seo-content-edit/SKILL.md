---
name: lead-seo-content-edit
description: >
  Use when SEO edit, 扩写, 改写, 去水分, 编辑文章, 润色, 内容审查,
  polish SEO draft, readability check, remove fluff, keyword
  density, or AI edit pass, including phase 9 SEO of this repo's
  lead run. Edit an approved lead-seo-content-gen draft with four
  operations (elaborate, rephrase, add helpful, remove fluff) and
  an eight-point check. Write the edit report and edited article
  under deliverables/lead/09-seo/. Read the ledger product_context
  first; invent no statistics, URLs, or testimonials; never paste
  skill examples into the output. Not for new articles from
  scratch, outlines, editorial guidelines, marketing copy polish
  (`marketing-copy-editing`), or phase navigation.
---

# SEO 成稿编辑（扩写、改写、去水分）

对已批准的 SEO 成稿做编辑：扩写薄段、改写生硬句、删空话、核验事实，并给出可打开的内外链建议，落到 `deliverables/lead/09-seo/`。缺证据标缺口，不编造。本步不写新文、不起大纲。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **输入**。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。硬依赖：已批准的 `deliverables/lead/09-seo/content.md`，或用户本轮贴出的成稿全文。软依赖（有则读，不阻塞）：`deliverables/lead/09-seo/editorial-guidelines.md`、`deliverables/lead/09-seo/outline.md`。闸门口径见 `skills/lead-generation/references/dependency-graph.md`，本文件不另写审批流程。优先项（连贯 / 可读 / 密度 / 帮助性）、改动容忍度或目标关键词仍缺到无法下笔：先看用户本轮；仍缺则打开 `skills/lead-interview/SKILL.md`（存在则按其做），否则停并写缺口。完成：能指出成稿、规范、大纲、目标关键词各依据哪一份；原文不拷进本仓库。硬依赖缺失且无 `user_waiver`、用户也未贴成稿 → 停，不从头写文章。
3. **八点编辑**。按「写法」对成稿走完八点；每点只使用四种操作：Elaborate、Rephrase、Add、Remove。成稿默认是逐章生成的，段落衔接是本步主责。用户点名只做其中几项时，未做项写入缺口，不算全量完成（有 `user_waiver` 除外）。多篇成稿需要隔离时 dispatch a subagent, else do it inline；默认一篇 inline。完成：八点各有结论（改了什么，或「无问题」）；拟改每一处都有类型与理由；无理由的改动撤销。
4. **查证链接与断言**。凡要保留或新加的统计、案例、外链：用网页搜索查证；需要原文则抓取指定 URL，确认页面存在且与锚文本相关。内链只指向产品上下文、用户给出的站点地图、或本仓库已有页面。用户要求对比竞争力时，用网页搜索看目标关键词的公开结果标题，记下可补的缺口；不据此整篇重写，不编造对手正文。搜索不可用 → 停止新增外链与新统计，语言层修改仍可保留，缺口写明。禁止为凑次数空搜。完成：拟用外链每条有 URL、访问日期、一句摘录；稿内数字能指回来源或已标「不可核验」；内链目标页有出处。
5. **落盘**。把修改应用到全文，写入「产出」所列文件。本 skill 不发布、不代替用户审批。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`。完成：主文件含编辑报告与完整编辑后文章；断言满足；教学支架原文零出现。

## 默认

- 产品事实只读 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止新增外链与新统计并写缺口，不编造。
- 数字、证书、客户名、项目结果：上下文或已抓取页里有才写入文章。没有就删断言或标「未在上下文出现」，禁止补造。
- 语气与可读性跟已批准的 `editorial-guidelines.md`；该文件缺失则用 down-to-earth + straightforward，可读性目标 Grade 6–7（清晰直接，不是幼稚化），并在缺口注明「规范未批准，暂用缺省」。不改成消费口语或俏皮话。
- 产品上下文里的技术词、认证名、型号、贸易术语保持原词；可读性不够时加一句解释，不替换成更「简单」的错词。
- 面客文章用语以产品上下文为准（缺省英语）；编辑报告用本轮语言（缺省中文）。同一段不中英混写。
- 上游成稿走 `skills/lead-seo-content-gen/SKILL.md`（文件存在时）；规范走 `skills/lead-seo-editorial-guidelines/SKILL.md`（文件存在时）；大纲走 `skills/lead-seo-outline-gen/SKILL.md`（文件存在时）。营销树文案精修走 `skills/marketing-copy-editing/SKILL.md`（文件存在时）。本文件不写新文、不起大纲、不定规范。
- 产出只进 `deliverables/lead/09-seo/`。

## 写法

四种操作，每处修改只标一种：

| 类型 | 何时用 | 材料从哪来 |
| --- | --- | --- |
| Elaborate | 段意对但过薄 | 大纲已列要点、产品上下文、已抓取页 |
| Rephrase | 句式生硬、重复、不顺 | 不新增事实 |
| Add | 读者缺一步能用的帮助 | 可核验来源；无来源的统计与案例不写。无数字的操作建议可以写 |
| Remove | 空过渡、同义反复、套话 | 删了更清楚就删；不为凑字回填 |

为读者改，不为字数改。删空话优于加填料。衔接做好时读者不应注意到过渡句。

**八点（按序，后一点改完回扫前一点）**

1. **段落衔接**。章与章、段与段是否接得上。逐章生成常见的断裂：上一节的结论没有被下一节接住、代词悬空、忽然换话题。补一句逻辑，不写「另一方面 / 综上所述」式重过渡。
2. **语气与可读**。是否符合规范的 Tone 与 Reading Level。缺省目标 Grade 6–7：短句为主（平均约 15–20 词）、常用词、主动语态、段长有变化、偶尔一词一句。不编造 Flesch 或年级精确分数；有可读性工具才记分数。朗读磕绊、从句堆叠、教科书腔 → Rephrase。规范若指定其他年级，以规范为准。
3. **帮助性**。每节是否至少有一个读者用得上的具体物：步骤、对比、已核验数字、定义、或可执行建议。只有泛述的节：有材料则 Elaborate / Add，没材料则标薄段缺口，不注水。
4. **外链位置**。哪些断言句适合指向第三方（行业协会、研究报告、政府数据、标准正文）。先标位置与拟用锚文本，再在步骤 4 核验 URL。目标 5 条已核验建议；找不到可靠源则少放并标注，禁止凑数。不编 URL、不链低质或无关页。外链是给读者核对用的，不把它写成排名开关。
5. **精简或展开**。空话段 Remove 或压短；过薄且有材料的段 Elaborate。同一意思不说两遍。
6. **标题与结尾**。H1 / H2 / 结尾是否具体、对人，而不是空泛主题词。结尾收一条可执行下一步（要规格 / 要报价 / 要样品，以上下文为准），不用 “In conclusion, [topic] is important.”
7. **关键词密度**。目标关键词（及大纲已列近义）合计约占全文词数的 1%–2%。算法：出现次数 ÷ 总词数。低于 1%：在标题、首段或收束处自然补一次，不硬插。高于 2%：Rephrase 掉堆砌。近义以大纲或用户本轮给出的列表为准，不自造一串同义词充数。密度是自检，不是排名承诺。
8. **小标题**。H2 / H3 是否能扫读、是否过泛。改成读者能预见本节答案的短句；不改成口号或俏皮话。

套话直接 Remove 或 Rephrase，不替换成另一套空话：game changer、let's dive in、in today's fast-paced world、unlock your potential、as previously mentioned、it's important to note。

## 产出

目录：`deliverables/lead/09-seo/`

主文件 `edited-content.md`：

```markdown
# SEO 成稿编辑

- source: 台账 product_context（不粘贴原文）
- draft: deliverables/lead/09-seo/content.md
- guidelines: deliverables/lead/09-seo/editorial-guidelines.md
- outline: deliverables/lead/09-seo/outline.md
- accessed:
- target_keyword:
- word_count_before:
- word_count_after:

## 编辑报告

### 八点结论

1. 衔接：
2. 语气与可读：
3. 帮助性：
4. 外链：
5. 精简或展开：
6. 标题与结尾：
7. 关键词密度：
8. 小标题：

### 修改汇总

| 章节 | 类型 | 原文摘要 | 改后摘要 | 理由 |
| --- | --- | --- | --- | --- |

### 关键词密度

- 目标词与近义：
- 出现次数 / 总词数 = ：

### 外链建议

| 锚文本 | URL | 访问日期 | 摘录 | 放在哪一句之后 |
| --- | --- | --- | --- | --- |

### 内链建议

| 锚文本 | 目标页 | 依据（上下文 / 用户 / 已有交付物） | 放在哪一句之后 |
| --- | --- | --- | --- |

### 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

### 缺口

### 下一步

## 编辑后文章

[完整成稿，面客语种]
```

断言（未满足则不算全量完成）：

- 报告与编辑后文章都非空；八点各有结论
- 修改汇总每一行有类型（Elaborate / Rephrase / Add / Remove）与理由；无「为改而改」行
- 外链建议每条 URL 已抓取且有访问日期；目标 5 条，找不到可靠源则少放并标注，禁止凑数
- 内链建议每条能指回已有页面；目标 3–5 条，站点页不够则按实有条数写并记缺口
- 密度已按出现次数 ÷ 总词数写出；越界已改或已说明为何保持
- 稿内数字有来源或已标不可核验 / 「未在上下文出现」
- 终稿无套话清单中的句子；无未解释的 `{{...}}`
- 教学支架原文零出现
- 未发布到网站；交付物不是已上线稿

## 例子

> 仅供理解，禁止引用到输出。

输入成稿规格表口径对、散文写另一套单位或互斥值。编辑应 Remove 散文错值，Rephrase 成与已核验规格句同一口径；不把「表对了所以营销段也可以留」当通过。规格层正确、文案层漂移，是本步主责。

输入成稿把电网法规专名写成省钱卖点，或写 seamless / uninterrupted / zero noise，或写「该改订哪一档」。编辑应 Remove 法规解读、绝对化和选型句；产品上下文有工况边界则 Elaborate 成可核验句，没有则标「不可核验」后删，不另编百分比、负载清单或兄弟互贬。

输入成稿用自造货架名（arena 当品类）、proven / tier-1 借光、或把 Dauerleistung 当放电时长。编辑应 Rephrase 成行业货架词（Heimspeicher / Gewerbespeicher 这类）并分开假朋友概念，只写己方动作；批发站原句不照抄。模板占位与同义反复 Remove。上一代叙事套到现行代、或一区口径写到另一区：标缺口，不圆过去。外链只写抓取过的地址。不要把本节句子粘进交付物。

## 易错

- 硬依赖成稿不在仍从头写文章，或把本文件当成 `lead-seo-content-gen`。
- 没读编辑规范就改语气，或把 B2B 规范改成消费口语。
- 为凑帮助性或密度编造统计、客户案例、认证。
- 外链、内链写未核验或不存在的 URL。
- 把精确可读性分数写进报告却没有测量工具。
- 为改而改，报告里没有理由。
- 删掉买家要看的技术词、认证名、型号。
- 用「另一方面 / 综上所述」假装衔接。
- 把教学例子或模型记忆当事实。
- 改完直接当成已发布，跳过用户审批。

## 清单

- [ ] 已读共用规则与 `product_context`；成稿有文件或用户原文
- [ ] 八点按序做完，每点有结论；每处修改有类型与理由
- [ ] 外链已抓取；目标 5 条，少放已标注，禁止凑数；未编 URL
- [ ] 内链只指向已有页面；页不够已写缺口
- [ ] 密度已计算；稿内数字有来源或已标不可核验
- [ ] 技术词未被「简化」错词替换；套话已处理
- [ ] 文件在 `deliverables/lead/09-seo/edited-content.md`；含报告与全文
- [ ] 教学例子原文未进入交付物；未发布
- [ ] 工具只写能力；多篇隔离时为 dispatch a subagent, else do it inline
