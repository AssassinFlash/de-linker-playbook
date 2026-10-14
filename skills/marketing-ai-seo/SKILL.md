---
name: marketing-ai-seo
description: >
  Use when the user asks for AI SEO, AI search, ChatGPT visibility,
  Perplexity optimization, Google AI Overviews, AEO, GEO, LLMO, answer
  engine optimization, generative engine optimization, AI搜索优化, or
  AI可见度, including phase 2 SEO of this repo's marketing run. Test
  whether the brand appears in answer engines, cite every visibility
  claim, and write a sourced content, schema, and entity action plan
  under deliverables/marketing/02-seo/. Read the ledger product_context
  first; invent no citations or scores. Not for classic keyword audits,
  programmatic page matrices, site architecture, or phase navigation.
---

# AI 搜索优化

实测品牌在回答引擎里是否被引用，把缺口写成带来源的内容、结构化数据与实体动作，落到 `deliverables/marketing/02-seo/`。评分为记录，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。读台账 `state/marketing-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）。把 `~` 展开为用户主目录，不要把 `~` 当相对路径。需要参数再读同目录 `fact-base/`。已有则读 `deliverables/marketing/01-foundation/` 的定位与竞品稿，以及 `deliverables/marketing/02-seo/` 的审计、站点蓝图、程序化页矩阵。完成：能指出品类、目标市场、产地、已知对手、买家角色、本站 URL 各依据哪几条；原文不拷进本仓库。站点未上线、无 URL、或品类/市场缺到无法构造查询则停并写缺口，不编造可见度。
3. **采集**。用网页搜索查证目标查询在公开检索与回答引擎中的表现；需要原文时抓取指定 URL 的正文（含可公开访问的引用来源页）。默认先搜再抓；搜索不可用则停止并写缺口。无法实际打开某回答引擎时，该平台行写缺口，不编造 appears。多查询或多域名并行时 dispatch a subagent, else do it inline。查询意图、下限与核验：读 `references/methodology.md`。完成：≥10 条可见度测试（每条含 query、平台、日期、appears、source）；≥5 个竞品域名有实际引用 URL 或显式缺口；≥5 个当前被引页面 URL；实体三项（品牌名、产地、品类）各有一次实测或缺口。
4. **分析**。只根据已记录测试写：可见度评分、引用缺口、实体覆盖、内容形态、三支柱动作。评分规则与形态表见 `references/methodology.md`。缺口必须能指回「竞品被引而本站没有」的具体查询。目标 URL 对齐已有站点蓝图，没有蓝图则只写 URL 模式并标缺口。完成：评分能回溯测试行；每条 P0 能指回一条采集记录。
5. **落盘**。写入下方路径与模板。策略与分析用简体中文；面客句子、URL、字段名、文件名按产品上下文（本仓库文件名保持英文）。完成：主策略稿含 6 个必需节；工作簿两表合计 ≥20 行且每行有 `source`；4 个执行附件非空；教学支架原文零出现。

## 默认

- 本 skill 产出进 `deliverables/marketing/02-seo/`。传统关键词审计、站点信息架构、程序化页矩阵不在这里做。
- 回答引擎默认覆盖：可公开核验的 AI Overview、可检索的引用来源页、用户本轮能打开的对话式回答引擎。三者引用机制不同，禁止写成同一套动作。
- 「出现在 AI 结果」必须来自本轮搜索或已抓取正文。禁止用模型记忆打可见度分。
- 目标渠道与站点技术栈以产品上下文为准，不预设某一建站或电商平台；schema 能否落地先核该技术栈，不能则写缺口。
- 数字、引用 URL、竞品出现与否只来自：产品上下文、用户本轮提供、已搜索或已抓取的公开页。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- **结构**：让内容可抽取——40–60 词直接回答段、表格优于长散文、H2/H3 对齐真实查询。
- **权威**：让内容可被引——统计、专家句、来源、认证、项目案例；上下文没有的数字写「未在上下文出现」。
- **存在**：出现在回答引擎会看的地方——行业目录、行业媒体、专业网络、目标渠道资料页；名单以产品上下文为准。
- 买家角色与查询优先级用产品上下文已有角色裁剪，不发明角色。
- 建议标 P0 / P1 / P2，每条含目标查询、目标平台、内容形态、URL 模式、工时、source。
- 程序化页只有在含独特规格、图片与询盘入口时才当作引用目标。

## 产出

主文件 `deliverables/marketing/02-seo/ai-seo.md`：

```markdown
# AI 搜索优化

- source: 台账 product_context（不粘贴原文）
- accessed:
- tests_n:
- visibility_score:

## AI 可见度现状诊断

## 竞品 AI 可见度对比

## 内容缺口分析

## 优化行动计划（P0 / P1 / P2）

## 结构化数据建议

## 实体建设路径

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 缺口

## 可验证断言
```

同目录：

- `ai-visibility-report.xlsx` — 从 `templates/ai-visibility-report.xlsx` 复制后填；不能写表时改同目录 `ai-visibility-report.json`。列与下限见 `references/methodology.md`。
- `execution/ai-seo/ai-visibility-audit.md`
- `execution/ai-seo/content-gap-plan.md`
- `execution/ai-seo/schema-checklist.md`
- `execution/ai-seo/entity-building-checklist.md`

主稿文末 5–10 条可验证断言。P0 必须能在 `ai-visibility-audit.md` 找到对应测试。

## 例子

> 仅供理解，禁止引用到输出。

输入写「多发内容提升 AI 可见度」。成稿应改成：分平台实测行业品类词（Heimspeicher / Gewerbespeicher 一类货架名，不是自造枢纽）；竞品被引的是品类页（定义段 + 类型表 + 品牌横切）、本站无对等 URL 时，P0 写「按站点蓝图补该页：40–60 词直接回答、类型表、H2 对齐该查询」，并附 query、平台、竞品引用 URL。不是加博客，也不是把批发顶栏原句搬过来。

输入写「FAQ 越多越好」。成稿应改成：机器可读看答句密度——问句下就地 20–40 词有后果的答，并落 FAQPage；只有标题、点进知识库才有正文的，记为路由器而非被引页。账号/运费/退货路由与技术问分桶；承诺数字只出产品上下文。不是堆空问句，也不是抄竞品天数、费率或免运门槛。

输入写「价格未公开，目录页不能当引用目标」。成稿应改成：匿名可浏览、价在登录墙后的品类页仍测 appears（规格面与类型筛可抽）。不是「必须公开价才做 AI SEO」，也不是把库存灯号或交期写成卖点。

查询用订货疑虑/临门一脚（接线、备电是否另配），不用升档问（够不够、以后是不是死路）。实体动作只列引擎已在引的学院/工具/目录形态，本站没有则写缺口，不编造计算器。

## 易错

- 没读产品上下文就按通用 SEO 开写。
- 未实测就打可见度分或写「已优化」。
- 把传统关键词排名当成唯一可见度指标。
- 用「多写文章」代替带查询与 URL 的缺口。
- 把三个回答引擎的引用机制写成同一策略。
- 只改本站、不核目录/媒体/目标渠道资料页对实体的贡献。
- 复制竞品正文，而不分析其被引结构。
- 用大量无规格、无图、无询盘入口的程序化页当引用目标。
- schema 清单不写实现方式与目标页，开发无法落地。
- 不核目标站点技术栈能否输出 JSON-LD 就下 schema 工单。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] ≥10 条可见度测试有 query、平台、appears、source；无法测试的平台已写缺口
- [ ] ≥5 个竞品域名有实际引用 URL 或显式缺口
- [ ] ≥5 个当前被引页面 URL；实体三项已测或已写缺口
- [ ] 优化行动 ≥20 条，每条有 priority、target_page、effort_days、source
- [ ] 主稿 6 节齐全；P0 能回溯审计附件
- [ ] 产出在 `deliverables/marketing/02-seo/`；表或 JSON 行含 `source`
- [ ] 终稿无占位 URL、无未核验「已出现」；教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
