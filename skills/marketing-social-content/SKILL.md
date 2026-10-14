---
name: marketing-social-content
description: >
  Use when the user asks for social media strategy, social calendar,
  multi-platform content, 社媒策略, 社媒日历, 多平台, Instagram B2B,
  Instagram content, Facebook page, TikTok B2B, TikTok manufacturing,
  社媒内容, 社交媒体策略, social selling, organic social, or a B2B
  foreign-trade social content plan, including phase 4 acquisition
  work. Collect competitor posts and platform benchmarks, then write a
  sourced pillar mix, 4-week calendar, post drafts, and hashtag sets
  under deliverables/marketing/04-acquisition/. Read the ledger
  product_context first; invent no engagement rates or follower
  counts. Not for a single LinkedIn post, paid ads, email sequences,
  转化文案库 (`marketing-copywriting`), or phase navigation.
---

# 社媒内容

把竞品公开帖与平台基准变成可执行的 B2B 社媒策略、日历与帖文草稿，落到 `deliverables/marketing/04-acquisition/social-content/`。缺互动数据就写缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若存在则读 `deliverables/marketing/03-content/` 的内容策略，以及 `deliverables/marketing/01-foundation/` 的竞品稿。已有 `deliverables/marketing/03-content/` 的 copy-library 或 snippets 对应 channel 行则复用其语气与 CTA，不另起价值主张。完成：能指出品类、目标市场、买家角色、品牌形态（公司品牌 / 出口经理个人品牌 / 两者）、可用视觉素材、已知竞品账号各依据哪几条；原文不拷进本仓库。品类、目标市场或买家角色缺到无法圈定平台则停并写缺口，不编造公司、粉丝、互动或对手事实。
3. **收集**。用网页搜索查证公开社媒与行业基准；需要原文时抓取指定 URL 的正文。默认先搜再抓；搜索不可用则停止并写缺口。用户已配置网页采集服务时，才用它抓公开页或动态页。多账号或多平台并行时 dispatch a subagent, else do it inline。每条记下 URL、访问日期、摘录。查询意图、数据门与核验：读 `references/methodology.md`。完成：≥20 条竞品帖（格式、主题、钩子、互动、来源）；≥5 个竞品账号且覆盖 ≥3 个平台（粉丝、发帖频率、内容组合、来源）；发帖频率由时间戳算出；平台基准与标签研究有来源或显式缺口。
4. **分析**。分开写、不要混：竞品社媒审计、分平台买家活跃度、内容支柱比例、钩子类型、一条素材到多平台的二次分发。支柱默认比例见 `references/methodology.md`，必须按已采集表现调整并引用来源，禁止原样套用默认表却不说明。完成：平台优先级有买家出现证据；每家竞品同时有有效格式与弱格式；二次分发图证明至少一种原始素材可衍生 ≥3 条平台原生帖。
5. **落盘**。写入下方路径。策略与分析用简体中文；面客帖文、标签、文件名按产品上下文语种（本仓库文件名保持英文）。完成：主稿与工作簿非空；日历 ≥30 行且 `copy_draft`、`visual_notes`、`hashtags`、`cta`、`source` 无空值；竞品审计 ≥5 行；帖文模板 ≥10 条；文末 5–10 条可验证断言；教学支架原文零出现。

## 默认

- 本 skill 产出进 `deliverables/marketing/04-acquisition/social-content/`。不要用它做付费投放或邮件序列。
- LinkedIn 单帖或选题走 `skills/lead-linkedin-topic-research/SKILL.md` 与对应 `lead-linkedin-*` 帖类型 skill（文件存在时）；本 skill 不下 Structure N。
- 目标渠道与平台名单以产品上下文为准。本方法覆盖 LinkedIn、Instagram、Facebook、TikTok、YouTube、Pinterest 等公开社媒，但排序必须按目标买家活跃度证据，不按运营偏好。
- 粉丝数、互动率、播放量只来自：产品上下文、用户本轮提供、已搜索或已抓取的公开页。没有数字就写「未在来源出现」，禁止估计后当事实。
- 竞品未出现的平台：要推荐必须同时写机会与风险，并标证据缺口。
- 展会与行业活动以产品上下文列出的名称为准；日期须核官方源，不写未核验的届次或人流。
- 表格式交付物每行有 `source` 或 `source_url`。终稿禁止 `TODO`、`TBD`、连续省略号占位。
- 工作簿从 `templates/social-calendar.xlsx` 复制后填行，不要另建产出根。

## 写法

- 先过收集门再写日历。门未过：只写缺口，不下频率或比例结论。
- B2B 买家（进口商、分销商、承包商、设计师、项目方）要规格、交期、认证与项目证据，不套用快消品种草模板。
- 漏斗用访问 → 询盘 → 样品 → 订单 → 复购，不用粉丝数替代询盘信号。
- 每条草稿同时有钩子、正文结构、视觉说明、CTA。询盘动作写「要规格 / 要方案」，不用注册或免费试用口吻。LinkedIn 行可从 lead 侧四类 CTA（评论型 / 连接型 / 私信型 / 混合）里选一类；其他平台不套这四类，仍用询盘动作。
- 一条工厂或项目素材拆成平台原生格式，不把同一段文字贴到所有平台。
- 日历必须有具体日期，禁止只写周次。

## 产出

目录 `deliverables/marketing/04-acquisition/social-content/`。

主文件 `index.md`：

```markdown
# 社媒内容策略

- source: 台账 product_context（不粘贴原文）
- accessed:
- platforms:
- competitors_n:

## 摘要

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 竞品社媒总览

## 平台优先级

## 内容支柱

## 发布频率与时段

## 二次分发

## 漏斗对齐

## 展会与节点（若上下文有）

## 行动计划（P0 / P1 / P2）

## 缺口

## 可验证断言

## 下一步
```

同目录一并写入（列与下限见 `references/methodology.md`）：

- `social-calendar.xlsx` — 从 `templates/social-calendar.xlsx` 复制；三表：Social Calendar ≥30 行、Competitor Social Audit ≥5 行、Post Templates ≥10 行
- `social-calendar.json` — 字段与表一致
- `posting-calendar.md` — 4 周、精确到日
- `post-drafts.md` — 10–20 条完整草稿
- `hashtag-strategy.md` — 分平台、已核相关性
- `content-pillars.md` — 3–5 个方向
- `platform-specs.md` — 尺寸、时长、字数上限、时段；数字来自已核官方说明

工作簿每行必须有非空 `source` 或 `source_url`。平台建议须含：买家出现证据、推荐频率、格式优先级、漏斗贡献。

## 例子

> 仅供理解，禁止引用到输出。

输入写「发一条项目案例轮播」。成稿应先放可核三件（应用与地点量级、谁负责哪一段、范围到哪停），再写一条带比较基准的结果；没有买方开口就停在指标块。角色写成职责（安装方 / 业主），不写裸名。不要编证言人名，也不要把同事的话改成客户口吻。视觉写现场安装范围，不写办公楼门头。

输入写「这周日历没主题」。成稿应把渠道摩擦当议题（登录才见价、交期非承诺、到货即验、缺陷单绕回厂商），钩子对准买家已有的下单卡点。不要种新疑虑，不要写成百科或选型作文，也不要把库存色点或时效口号当卖点。

输入写「标签和钩子要显得高端」。成稿应跟批发目录用词（家用储能、工商业储能、套餐），帖文换到兄弟产品应不成立。不要自造赛道名，不要套 one-stop shop / skip the middleman / we are your bridge。身份停在工程 BOM、配对核验、调试与质保协调，不要自称制造商、备件库或自有质保承保。CTA 写「要规格 / 要方案」，不要注册或免费试用口吻。

日历主帖带上述字段或摩擦，一条素材拆成平台原生格式。不要写「打造爆款内容矩阵」，也不把本节句子粘进交付物。

## 易错

- 没读产品上下文就套通用社媒日历。
- 未验证目标买家是否使用某平台就推荐 TikTok 或 Instagram。
- 用粉丝数、点赞数替代访问→询盘→样品→订单。
- 编造互动率或粉丝数，而不是标缺口并建议 4 周基线追踪。
- 日历只有主题占位，没有文案、视觉说明、CTA 和来源。
- 忽略平台约束，把 LinkedIn 长文原样贴到短视频平台。
- 竞品未使用的平台直接铺开，不写机会与风险。
- 支柱比例照抄默认表，不引用竞品表现。
- 把教学例子或模型记忆当事实。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] ≥5 个竞品账号、≥3 个平台、≥20 条帖，频率来自时间戳，每条有来源
- [ ] 平台优先级有买家活跃度证据；未覆盖平台已写机会与风险或缺口
- [ ] 支柱比例已按数据调整或显式说明沿用原因
- [ ] 日历 ≥30 行；模板 ≥10；草稿 10–20；二次分发 ≥3 条原生帖
- [ ] 产出在 `deliverables/marketing/04-acquisition/social-content/`；表行 `source` 非空
- [ ] 无占位符；教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
