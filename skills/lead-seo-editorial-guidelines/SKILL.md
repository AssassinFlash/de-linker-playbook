---
name: lead-seo-editorial-guidelines
description: >
  Use when editorial guidelines, tone guide, readability standards,
  content style guide, brand voice, writing rules, EEAT guidelines,
  编辑规范, 文章风格, 内容标准, SEO writing standards, 语气规范,
  可读性标准, or when setting SEO tone, reading level, formatting,
  and avoidance rules before any outline or draft. Write a
  five-dimension editorial standard (tone, reading level, avoid,
  text format, tips) under deliverables/lead/09-seo/. Foundation of
  this repo's lead SEO run: guidelines then outline then draft then
  edit. Read the ledger product_context first; invent no conversion
  statistics. Not for article outlines, body copy, editing an
  existing draft, editorial calendars, SEO audits, or phase navigation.
---

# SEO 编辑规范

在写大纲和成稿之前，为获客站 SEO 文章定语气、可读性、避免项与版式，落到 `deliverables/lead/09-seo/`。这是 SEO 四件套的第一步（规范 → 大纲 → 成稿 → 编辑）；本文件不写大纲、不成稿、不编已有文章。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。读台账 `state/lead-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。原文不拷进本仓库。已有风格指南或上游定位则读用户本轮给出的文件，以及 `deliverables/lead/01-icp/`、`deliverables/lead/05-usp/` 中已批准稿（有则用，无则不挡）。核心只要两项就能开写：品类/利基、目标读者。品牌语气、已有风格指南、阅读负担用户给了再用。缺核心两项：先看用户本轮消息；仍缺则停并只要这两项。需要结构化补问时打开 `skills/lead-interview/SKILL.md` 并按其步骤做，不要在本文件另写问卷。完成：能指出读者与语气各依据哪几条；缺项标「未在上下文出现」。

3. **查证**。用网页搜索查证三类公开口径；需要原文则抓取指定 URL 的正文。查询年份用环境当前公历年。三类：
   - 可读性与扫读：公开讨论「一次能看懂 / 扫读 / 理解成本」与停留或转化的关系。记下 URL、访问日期、摘录。不要预设某一家工具的年级分数线。
   - 内容质量：当前公开的有用内容与 E-E-A-T（经验、专业、权威、可信）口径，当作质量门，不当作某年更新清单。
   - AI 成稿反模式：当前公开的套话与「读起来像机器」的写法。
   概念型最低查证见 `skills/lead-generation/references/search-protocol.md`；达不到不编造、不空搜凑数。搜不到的主张标 unverified。搜索不可用：五维规范仍可按「写法」落盘，但转化率、平台更新、检测器分数一律不写或标缺口。需要隔离时 dispatch a subagent, else do it inline。完成：搜索日志非空，或已写明搜索缺口；无出处数字为零。

4. **定五维**。按「写法」写出 Tone、Reading Level、Avoid、Text Format、Tips。语气最多 2 个；选型与否决表见 `references/tone-guide.md`。每条规范可检查：套上与不套上，成稿应能看出差别。「写好一点」不算规范。已有风格指南与本方法冲突时，记下冲突与取舍，不悄悄覆盖。完成：五维都有理由；可读性目标明确且可检查；Avoid 覆盖源方法 8 条反模式。

5. **落盘** `deliverables/lead/09-seo/editorial-guidelines.md`，用「产出」模板。策略说明用中文；五维规则句与组装块用英文（供下游成稿指令粘贴）。每条标 P0 / P1 / P2。完成：主文件非空；组装块可整段复制；教学支架原文零出现。

6. **出门检查**。对照清单。完成：清单可逐条勾选，或已记录 `user_waiver`。

## 默认

- 本 skill 无硬上游，是获客 phase 9 入口。下游串行：`lead-seo-outline-gen` → `lead-seo-content-gen` → `lead-seo-content-edit`。下一方法打开对应 `SKILL.md`（文件存在时）；本文件不写大纲与正文。管线位置见 `skills/lead-generation/SKILL.md`。
- 产品事实只读 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不写工具 ID。单文件工作 inline 做完。
- 数字、转化率、平台质量更新：产品上下文或已抓取页里有才写。没有就写「未在上下文出现」或 unverified，禁止补造。
- 可读性目标必须写明（谁能一次看懂、句子与段落约束、术语是否首现解释）。禁止把未核验的工具分数线写成门槛。
- 面客语种以产品上下文为准；组装块默认英文。同一段不混用。
- 网站整站 SEO 审计走 `skills/marketing-seo-audit/SKILL.md`（文件存在时）。编辑日历、选题集群与 content brief 走 `marketing-content-strategy`。本文件只管获客 SEO 文章的编辑规范，不写日历、选题集群或成稿。
- 产出只进 `deliverables/lead/09-seo/`。

## 写法

**逐节生成（写入规范文档，供下游遵守）。** 不要用一条指令生成整篇。先大纲、再按章节写。一次出全文时模型会滑向套话，人工只能整篇返工。大纲决定质量上限；规范里必须写明这条，而不是把「写一篇」留给下游自由发挥。

**Tone。** 最多 2 个。多了指令互相打架，输出不稳定。稳定档：Down-to-earth、Straightforward、Authentic、Warm。默认不要：Professional（high-register，aim to / elevate / crucial，可读性差）、Witty、Humorous、Approachable（方差大）。Conversational 偶发自然、偶发浮夸，用则必须人工复看，并在规范里写明这条风险。不要要求「写成某名人的风格」——方差大，面客英文不稳。组合建议见 `references/tone-guide.md`。

**Reading Level。** 先写读者是谁（从产品上下文取），再写可检查约束：短句、常见词承载复杂规格、术语首现必解释、段落可扫读。这是把专业内容写清楚，不是写给儿童。转化率或「某年级转化最高」：有已抓取来源才写进理由，并带来源与日期；没有就不写百分比。禁止用未核验分数线冒充已证实门槛。

**Avoid（8 条都要进规范，可补当前套话，不可删源方法条）。** Being too salesy；Getting too hyped；Sounding like a cringey writer；Being robotic and repetitive；Using worst humor；Cliche phrases；Using formula language；Using exclamations。模型默认成稿容易踩这些；规范不写，下游就会长这样。

**Text Format。** 短段落；偶尔单句成段；需要时用列表；句子长短要有变化，穿插短句。目的是扫读，不是把正文拆成碎片。

**Tips。** 新术语先定义。人称默认 you（对读者）与 we（对公司）；个人署名专栏才用 I。断言要有来源。禁用 AI 高频套话，以 game changer、let's dive in 为代表；查证阶段若发现新套话，补进 Avoid 或 Tips，并带来源。

**可检查。** 每条规范应能改变输出。只推荐多次跑下来稳定的语气；高方差语气必须带警告。规范不要严到每篇都一个味道。

## 产出

目录：`deliverables/lead/09-seo/`

主文件 `editorial-guidelines.md`：

```markdown
# SEO 编辑规范

- source: 台账 product_context（不粘贴原文）
- accessed:
- audience:
- existing_style_guide:

## 摘要

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 搜索日志

## Editorial Guidelines

### Tone

### Reading Level

### Avoid

### Text Format

### Tips

## Assembled Guidelines

（英文，可整段复制到下游成稿指令）

## 逐节生成

## Tone Reference

## 优先级（P0 / P1 / P2）

## 可验证断言

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- Tone 1–2 个，每个有理由；未用默认禁止档，或已写明例外与风险
- Reading Level 有明确、可检查的目标与读者依据；含数字的转化或年级主张有 URL，或已标 unverified / 缺口
- Avoid 覆盖上述 8 条反模式
- Text Format 含短段落与句长变化
- Tips 含术语定义、人称、来源、AI 套话
- Assembled Guidelines 为英文整段，可复制
- 「逐节生成」已写入，且禁止一条指令出全文
- 每条规范有 P0 / P1 / P2
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入只有「B2B 买家、要专业一点」。规范应写成最多两个稳定语气（如 down-to-earth + straightforward），并写明 Professional 会抬高用词、降低扫读。可读性写成「非技术采购也能扫完规格段，术语首现解释」，不要写成未核验的年级分数或转化百分比。

Tips 应写成：品类名跟货架上的行业词走（家用储能 / 工商业储能 / 集装箱储能），不要自造货架标签；柜体、机架、集装箱三类词分开写。假朋友单独列——放电时长用小时或倍率，不要拿「持续功率」去翻 duration；混合逆变器是设备名，不要写成未点名设备的 hybrid system。Avoid 补上借来的光环词（proven、tier-1、leading）和把一国法规名词堆进另一国英文标题。

跨境面：同一货架在不同市场是不同品类名，规范应写「按目标市场用语，不机翻货架名」；并网规则、可调控用电、持证电工留在该制度里，不要译成美式 utility 话（电表前后、投资税收抵免、购电协议）。

数字与断言：Tips 写「每个数字须能指回产品上下文，上下文没有的不写」。Avoid 写明禁绝对化（zero / seamless / uninterrupted）和禁选型建议（该选哪台 / 适合哪类项目）。家族共性句可写，但不得包装成本页独有。组装块用英文规则句，不要把本节句子粘进交付物。

## 易错

- 没读产品上下文就定语气，或把教学例子当品牌口吻。
- 同时点三个以上语气，或点 Professional / Witty / Humorous 却不写风险。
- 要求「写成某名人的风格」。
- 用未核验的工具分数线或转化率当可读性门槛。
- Avoid 只写「别写得像 AI」，不列 8 条反模式。
- 规范含糊（「写好一点」），下游无法执行。
- 一条指令出全文的原则没写进交付物。
- 编造 E-E-A-T 年份更新或检测器分数。
- 把本文件当成大纲器或成稿器。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 读者与利基有依据；缺核心两项已停并写缺口
- [ ] 三类查证有日志或已写搜索缺口；无出处数字为零
- [ ] 语气最多 2 个；选型已对照 `references/tone-guide.md`
- [ ] 可读性目标明确、可检查；未把未核验分数线当门槛
- [ ] Avoid 8 条在；版式与 Tips 齐全；组装块为英文可复制
- [ ] 逐节生成已写入；每条有 P0 / P1 / P2
- [ ] 文件在 `deliverables/lead/09-seo/editorial-guidelines.md`
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
