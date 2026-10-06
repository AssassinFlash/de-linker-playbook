---
name: lead-seo-content-gen
description: >
  Use when expanding outline sections into prose, writing article body text,
  SEO 成稿, write article, content generation, expand outline,
  section-by-section writing, SEO content writing, generate article body,
  write sections, 内容生成, 文章撰写, 逐章节写作, or draft article
  content, including phase 9 SEO of this repo's lead run. Expand each
  approved outline heading into full paragraphs under
  deliverables/lead/09-seo/; never dump the whole article in one shot.
  Hard dependency: an approved lead-seo-outline-gen outline. Read ledger
  product_context first; invent no statistics. Not for creating outlines,
  polishing existing drafts, or phase navigation.
---

# SEO 成稿（逐节展开）

按已批准大纲一节一节写成面客 SEO 正文，落到 `deliverables/lead/09-seo/`。缺证据标缺口，不编造。本文件只写成稿：不写大纲，不润色已有草稿。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。硬依赖：已批准的 `deliverables/lead/09-seo/outline.md`（`lead-seo-outline-gen`）。软依赖（有则读，不阻塞）：`deliverables/lead/09-seo/editorial-guidelines.md`。用户本轮给出的大纲全文、规范、先写哪几节、要嵌入的例子或数据、每节字数，来源记「用户本轮」。先写范围、字数或必须嵌入的数据点仍缺到无法下笔：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不在本文件另写问卷。完成：能指出目标关键词、文章类型、各节要点、语气与可读性各依据哪几条；原文不拷进本仓库。硬依赖文件缺失、用户本轮也未给出对应大纲全文、且无 `user_waiver` → 停。

3. **列节**。按大纲顺序列出将写的节：引言、每个 H2（及其 H3）、结论、FAQ（大纲含 FAQ 才列入）。每节记下要点与目标字数：大纲或用户本轮指定优先，否则用「默认」里的区间。禁止增删大纲里的 H2。完成：节清单与大纲一一对应；每节有要点和字数目标。

4. **查证**。将对写入正文的数字、标准、对比、外链，用网页搜索查证；需要原文则抓取指定 URL。顺带收集可链到的权威第三方页。正文不用搜到的他人文章原句。搜索不可用：面客正文不写无来源统计、不编外链，缺口写明。禁止为凑次数空搜。禁止编造 URL。单篇 inline 做完；多篇需隔离时 dispatch a subagent, else do it inline。完成：拟用数字与外链有 URL 与访问日期，或已决定不用；`## 搜索日志` 有行（正文无统计也无外链则写「本轮未检索」）。

5. **逐节写 H2**。同一篇文章必须按节写，写完一节过完该节完成条件再写下节；禁止一次生成整篇再回头填。你就是执笔人，不要把要点再包成「发给另一个模型的指令」。每节：从该节大纲要点写起 → 套已读规范的语气与格式（规范缺失则用「写法」）→ 写在目标字数区间内（写不满不注水，实际字数记入成稿记录）→ 嵌入至少一项有证据的 helpfulness（可执行提示、已核验数字、对比、引用、来自上下文或本轮查证的例子）→ 自检短句、常用词、主动语态。节与节之间写过渡，但每一节单独读仍有收获。用户本轮要求每节停下来确认时才停；默认连续写完，内部仍分节。完成：每个拟写 H2 都有成稿；字数有变化；无大纲外的 H2。

6. **引言、结论、FAQ**。这三块在 H2 之后写，组装时仍放回大纲位置。引言：钩子（已核验数字、大胆问题或短事实；不编未发生的轶事）+ 点到或呼应主关键词，默认 100–150 词。结论：收束要点 + 一个可执行 CTA，默认 100–150 词。FAQ：只写大纲已列的问题；每答默认 50–100 词，不读全文也能成立。大纲漏了引言或结论仍要写；大纲没有 FAQ 则不写。完成：引言有钩子；结论有 CTA；FAQ 与大纲问题对应或已标明「大纲无 FAQ」。

7. **组装质检落盘**。按大纲顺序拼成一篇：标题 → 引言 → 正文 → 结论 → FAQ。对照清单后写入 `deliverables/lead/09-seo/content.md`。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批、不代替发布。精修走 `skills/lead-seo-content-edit/SKILL.md`（文件存在时），本步不代替编辑 skill。完成：主文件非空；大纲节无漏；教学例子原文零出现。

## 默认

- 产品事实只读台账 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止写无来源统计与外链，并写缺口，不编造。
- 编辑规范有则从其 Tone / Reading Level / Avoid / Text Format / Tips。缺失时用「写法」里的兜底，并在缺口写「未读到已批准编辑规范」。
- 字数兜底：引言 100–150 词；每个 H2 150–400 词；结论 100–150 词；FAQ 每答 50–100 词。大纲或用户本轮另有指定则从其指定。
- 外链目标：写入不少于 5 条本轮已核验的第三方 URL；核验不足则按实有写入并在缺口写明，不编造链接凑数。
- 面客语种以产品上下文为准，缺省英语；策略、日志、缺口用本轮语言（缺省中文）。同一段不混用。
- 面客正文禁止残留 `{{...}}` 或 `[待补充]`；缺事实则删该句，把缺口写在成稿记录。
- 单篇 inline 逐节写完。产出只进 `deliverables/lead/09-seo/`。
- 进度只认台账。本文件不发布到站点。

## 写法

- 大原则：一节一节写。一次出整篇会把各节写成同一套空泛腔，后续只能整篇来回改。
- 每节必须能单独成立，不是下一节的铺垫。
- 每节至少一项 helpfulness。没有来源的数字不要写，改用可执行提示、对比或已核验例子。
- 语气兜底：接地气、直说；规范另指定 1–2 个 Tone 则用指定的。短段；必要时一条单独成段；该用列表再用列表；句子长短要有变化。
- 可读性兜底：按规范的年级写；规范缺失则按大约 6–7 年级操作——平均句长约 15–20 词、常用词、主动语态、具体名词。朗读像教科书就拆句。这是可检查的写法，不要求特定打分工具。
- 新术语当场解释。主张能回溯来源。第一人称 I / you 仅在规范要求时用；规范没写则用直说的 you，不装专家口吻堆 I。
- 先结果后规格：规格接到买家可感到的结果，不堆参数。空话（high quality、world-class、leading）无证据则删。
- 目标关键词及其同义/相关词按大纲自然出现：标题、引言、以及大纲已安排的节。不靠堆砌次数交差。大纲若有语义关键词，分散进相关节，不在同一段填满。
- 引言钩子要具体。结论 CTA 接到可执行下一步（要规格、要报价、要样品、读相关页）；不用注册 / 免费试用 / 订阅口吻；不承诺本轮不存在的材料。
- 节与节用过渡句接上，但不写「as previously mentioned」一类撑场句。

## 产出

主文件 `deliverables/lead/09-seo/content.md`。面客正文在分隔线之上，可整段复制；成稿记录在分隔线之下，不粘进站点。

```markdown
# [Article Title]

[Introduction]

## [H2 from outline]
[section body]

## [Conclusion heading from outline, else Conclusion]
[conclusion body]

## [FAQ heading from outline, else FAQ]
**[Question]**
[Answer]

---

# 成稿记录

- source: 台账 product_context（不粘贴原文）
- accessed:
- outline: deliverables/lead/09-seo/outline.md
- guidelines: deliverables/lead/09-seo/editorial-guidelines.md | missing
- target_keyword:
- article_type:

## 分节
| section | word_count | helpfulness_type | notes |
| --- | --- | --- | --- |

## 关键词
- target_in_title:
- target_in_intro:
- related_terms_used:

## 可读性
- rule_applied:
- check: 短句 / 常用词 / 主动语态 / 朗读不像教科书

## 来源
| 声明 | URL 或上游文件 | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 外链
| URL | 写入位置 | 核验日期 |

## 搜索日志
| 查询或 URL | 日期 | 结论 |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 大纲每个 H2 都有对应成稿；无擅自增加的 H2
- 逐节写成，不是一次出整篇
- 每个 H2 至少一项 helpfulness；无来源统计未写入面客正文
- 引言有钩子；结论有 CTA
- 外链均为本轮核验 URL；不足 5 条已在缺口写明
- 面客正文无未解释占位符；教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入是已批准大纲里一节「How to compare lead times」，要点只有「ask for production calendar, not a single number」。成稿应把该要点写成 150–400 词、带一条可执行问法或已核验来源，而不是一次写出整篇文章，也不要用「In today's fast-paced world」开场。缺交期天数就不要编天数。不要把本节句子粘进交付物。

## 易错

- 一次指令写出整篇，再回头填节。
- 没读已批准大纲或产品上下文就发明节名、规格、案例。
- 把教学例子或搜到的他人文章原句写入交付物。
- 用 game changer、let's dive in、in today's fast-paced world、unlock your potential、In conclusion、it's important to note 撑场。
- 推销腔、假高潮、感叹号堆砌、同一句式反复。
- 各节一样长、一样空。
- 把关键词密度当完成条件，堆砌目标词。
- 编造统计、客户引言、证书、URL 或未发生的轶事来凑 helpfulness。
- 规范 Avoid 列表里的写法原样出现。
- 把本文件当成大纲生成器或成稿润色器。
- 终稿残留 `{{...}}`，或把成稿记录里的缺口假装成已核实数字。

## 清单

- [ ] 已读共用规则与 `product_context`；硬依赖大纲已读或已停并写缺口
- [ ] 节清单与大纲一一对应；无擅自增删的 H2
- [ ] 有统计或外链的句子均已查证；搜索不可用时未编造
- [ ] 各 H2 逐节写成，每节有 helpfulness，字数有变化
- [ ] 引言有钩子；结论有 CTA；FAQ 仅在大纲有时出现
- [ ] 目标词自然出现在标题与引言；未靠堆砌交差
- [ ] 文件在 `deliverables/lead/09-seo/content.md`；面客正文无占位符
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
