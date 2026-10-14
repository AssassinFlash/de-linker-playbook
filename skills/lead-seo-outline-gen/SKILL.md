---
name: lead-seo-outline-gen
description: >
  Use when article outline, SEO outline, content outline, heading
  hierarchy, article framework, content planning, keyword outline, 大纲,
  文章结构, 内容规划, 文章大纲, choosing how-to / listicle / ultimate
  guide / thought leadership, or mapping sections before writing body
  text, including phase 9 SEO of this repo's lead run. Research ranking
  pages and related questions, then write a typed outline under
  deliverables/lead/09-seo/. Requires approved editorial guidelines.
  Read the ledger product_context first; invent no competitor headings
  or statistics. Not for setting editorial tone, writing article body,
  editorial calendars, or phase navigation.
---

# SEO 大纲生成

按四种文章类型之一，在写正文之前产出 SEO 大纲（标题层级、意图覆盖、竞品缺口），落到 `deliverables/lead/09-seo/`。不写编辑语气规范，不写正文。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入与闸门**。读台账 `state/lead-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。硬依赖：已批准的 `deliverables/lead/09-seo/editorial-guidelines.md`。缺失且无 `user_waiver` → 停；打开 `skills/lead-seo-editorial-guidelines/SKILL.md`（存在则按其做），不自造语气规范。软依赖（有则读，不阻塞）：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/04-market/competitor-positioning.md`；若 `deliverables/marketing/03-content/` 已有日历或选题集群（`content-calendar.md`、`topic-clusters.md`、`content-strategy.md`），用作选题输入，没有则独立。用户本轮给出的目标关键词、文章类型、受众、文章目标一并用作本轮输入。这四项仍缺：先看本轮消息；仍缺则打开 `skills/lead-interview/SKILL.md`（存在则按其做），否则停并写缺口。不要在本文件另写问卷。原文不拷进本仓库。完成：能指出关键词、受众、语气各依据哪几条；能复述上游 Tone 与可读性约束。

3. **调研**。用网页搜索查证目标关键词的自然结果；需要原文则抓取可打开的前 3 条 URL，抽出 H1/H2、覆盖深度、是否有 FAQ / 对比 / 步骤。再搜相关问题（结果页若出现 People Also Ask 则记下；相关搜索；买家问句）。映射主 / 次 / 再次意图（信息、导航、交易、商业调查）。意图与事先假定不符 → 写入交付物并调整类型或关键词，不硬套。日志格式见 `skills/lead-generation/references/search-protocol.md`。搜索不可用 → 停并写缺口，不编造竞品标题或搜索量。多页并行时 dispatch a subagent, else do it inline。完成：至少 3 个竞品页有 URL、访问日期、H2 摘录，或已把不足写入缺口；意图表非空；`## 搜索日志` 有行。

4. **定类型**。只准四种。用户已点名且在池内 → 用该类型；若与步骤 3 的主意图明显冲突，报告冲突并建议改类型，不在未说明的情况下改掉。未选：按主意图建议一种并写一句理由；本轮能问则只问一句；用户已说直接做或本轮不能问 → 取建议，交付物写「类型未经用户确认」。禁止自造第 5 种。Thought Leadership 必须有一条可陈述的观点；没有观点则改类型或停。读对应模板后再进入下一步：

   | 类型 | 模板 | 适合 |
   | --- | --- | --- |
   | How-to | `references/howto-template.md` | 逐步任务、流程 |
   | Listicle | `references/listicle-template.md` | 清单、工具/要点/错误合集 |
   | Ultimate Guide | `references/ultimate-guide-template.md` | 支柱页、全面覆盖 |
   | Thought Leadership | `references/thought-leadership-template.md` | 观点、趋势判断 |

   完成：一种类型、对应模板已读；冲突已记录或已排除。

5. **初稿**。按该模板产出 Title (H1)、Meta Description、Introduction 要点、Main Sections（H2 + 要点）、Conclusion / CTA、按意图分组的语义词。标题自然含目标关键词。每个 H2 写一句存在理由（对应哪条用户问题）。完成：必含块齐全；子弹点写将写入正文的事实或步骤，不写「讨论…的重要性」。

6. **增强**。对照已抓前 3 名：补他们没答的问题、没写的深度、没给的对比。每节映射至少一种已识别意图；映不上的节删或并。每节至少一个 helpfulness 标记（可执行例子、对比、引用、表、实用提示；统计有来源才写数字，否则只标 `[待补充]` 或不写）。默认加 FAQ，问句必须来自本轮相关问题；凑不出真实问句则标缺口，不编 FAQ。目标是比已抓页更覆盖意图，不承诺排名。完成：竞品缺口 ≥3 条且每条能指回已抓页（缺问句 / 缺深度 / 缺对比都算）；做不到则停并写缺口，不编空白；无空 H2。

7. **落盘**。对照清单写入 `deliverables/lead/09-seo/outline.md`。本 skill 不写正文。下一步打开 `skills/lead-seo-content-gen/SKILL.md`（文件存在时）。完成：主文件非空；教学支架原文零出现。

## 默认

- 产品事实只读 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止并写缺口。
- 面客大纲（Title、Meta、H2、要点、FAQ）用产品上下文的面客语种，缺省英语；策略、竞品分析、意图说明用本轮语言（缺省中文）。同一段不混用。
- 年份：只有时效性主题（工具、趋势、当年法规）才写入标题；取运行当日公历年，不写死某一年。
- 语义词来自本轮搜索与相关问题，按意图分组。类型模板给的是目标区间，不是配额；不够则少写并标缺口，不用近义词凑数。
- CTA 跟产品上下文；缺省「要规格 / 要报价 / 要样品」或指向站内已有相关篇。不用注册、免费试用、订阅。
- 内链只建议产品上下文或已抓取页里真实存在的 URL，不编链接。
- 单篇 inline 做完；多 URL 需隔离时 dispatch a subagent, else do it inline。
- 产出只进 `deliverables/lead/09-seo/`。Markdown only。
- 验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`。本 skill 不代替审批、不写正文。

## 写法

- 每个 H2 必须回答一个真实用户问题；去掉后文章不减值的节不写。
- 每节映射至少一种已识别搜索意图。
- 竞品分析是找缺口，不是模仿对方目录。
- H2 具体。不用 Getting Started、Key Considerations、空的行业洞察。
- 非 Listicle：How-to 5–8 步；Ultimate Guide 5–8 块；Thought Leadership 3–5 柱。Listicle 的 H2 数必须等于标题里的数字。
- 目标关键词自然出现在 H1；不要每个 H2 都塞同一词。
- 子弹点写将写入正文的事实、步骤、对比点。
- FAQ 问句用本轮相关问题改写，不为摘要卡编造问答。
- 可读性与语气只引用上游 `editorial-guidelines.md`，不在本文件另定 Tone。

## 产出

主文件 `deliverables/lead/09-seo/outline.md`。用户点名文件名则用该名。

```markdown
# Article Outline

- source: 台账 product_context（不粘贴原文）
- accessed:
- target_keyword:
- article_type: How-to | Listicle | Ultimate Guide | Thought Leadership
- type_confirmed_by_user: yes / no
- buyer_language:
- editorial_guidelines: deliverables/lead/09-seo/editorial-guidelines.md

## Target Keyword

## Article Type

## Title (H1)

## Meta Description
（目标 150–160 字符，含关键词；写出字符数）

## Introduction
Hook / context / preview（要点，不是成稿）

## Main Sections
### H2: …
- 要点
- 存在理由（用户问题）
- 意图：信息 / 导航 / 交易 / 商业调查
- helpfulness：例子 / 对比 / 引用 / 表 / 提示 / 统计来源

## FAQ
问句来自本轮相关问题

## Conclusion
Recap + CTA

## Semantic Keywords
按意图分组，一行一词

## Competitor Gap Analysis
| 竞品 URL | 已覆盖 | 缺口 | 我们补什么 |

## Search Intent Coverage
主 / 次 / 再次意图；各 H2 映射

## 搜索日志
| 查询或 URL | 日期 | 结论 |

## 缺口

## 可验证断言
```

断言（未满足则不算全量完成）：

- 类型在四种之内，模板结构已遵循
- Title 自然含目标关键词；Meta 写出字符数
- 每个 H2 有存在理由、至少一种意图、至少一个 helpfulness 标记
- 竞品表 ≥3 行，每行 URL 非空；缺口 ≥3 且能指回已抓页
- 语义词按意图分组，词来自本轮搜索，无凑数近义词串
- FAQ 问句能指回搜索日志，或已标「相关问题未找到」
- 含数字的标记有来源或 `[待补充]`
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入是「储能选购 / 工商业储能」支柱大纲。选题集群按批发货架的行业树分柱：家用储能与工商业储能分开，工商业再按类型（一体机、集装箱、带变流器的模块、不带变流器的模块）各成门；H1 用行业词（Home storage / Commercial storage，德文面客则 Heimspeicher / Gewerbespeicher）。不要用自造货架名（arena、energy infrastructure）当柱名，也不要把德制度（电网登记、运营商手续）写成美式 behind-the-meter 节。Main Sections 的 H2 仍对本轮相关问题开门——相关问题优先取搜索补全形状（地理+批发、品牌+批发、逆变器+电池+兼容），例如「报价前先锁定逆变器与电池的配对」；不要写成 Getting Started / Key Considerations / Compatibility Overview，也不要把批发导航或学院课表改写成自己的目录。

FAQ 问句来自本轮相关问题，形状是订货疑虑或临门一脚（这一单已经卡住的），写成安装工能看见的症状或任务。不要自造「What is [keyword]?」，不要写升档问（这台够不够、该不该改订另一台），不要把店级分桶（账号、运费、退货）塞进产品 how-to。批发 FAQ 若是主题标签（Warranty、Shipping），改写成任务句。统计格只在已抓页或产品上下文有数字时填，否则 `[待补充]`。不要把本节句子粘进交付物。

## 易错

- 没抓竞品页就写大纲，或把对方 H2 改写后当自己的结构。
- 跳过意图分析，或 SERP 意图已变仍硬套事先选的类型。
- 没读已批准的编辑规范就定语气。
- 用空 H2、每个标题重复同一关键词、子弹点只写「discuss…」。
- 标题数字与 Listicle 条目数不一致。
- 为凑语义词或 FAQ 编造近义词和问句。
- 编造统计、搜索量、案例或未持有的认证。
- CTA 写成注册 / 试用 / 订阅。
- 在本 skill 里写正文，或把教学例子原文写入交付物。
- 硬依赖缺失且无 `user_waiver` 时继续。

## 清单

- [ ] 已读共用规则、`product_context`、已批准编辑规范；原文未拷进本仓库
- [ ] 前 3 条可打开结果已抓取 H2；搜索日志非空；缺搜索已停并写缺口
- [ ] 类型在四种之内；模板已遵循；意图冲突已处理
- [ ] 每个 H2 有存在理由、意图映射、helpfulness 标记
- [ ] 竞品缺口 ≥3 且能指回已抓页；FAQ 问句有来源或已标缺口
- [ ] 语义词按意图分组，未用近义词凑数
- [ ] Title 含关键词；Meta 有字符数；CTA 非 SaaS 口吻
- [ ] 文件在 `deliverables/lead/09-seo/`；未写正文
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
