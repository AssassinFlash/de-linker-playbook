---
name: marketing-programmatic-seo
description: >
  Use when the user asks for programmatic SEO, pSEO, scalable landing
  pages, page matrix, template pages, batch pages, 批量页面, 程序化SEO,
  程序化落地页, or a template-driven matrix of product, application,
  location, or comparison pages. Collect SERP and catalog evidence,
  design unique page types with URL patterns, hub-and-spoke links, and
  indexation rules, and write the strategy plus page matrix under
  deliverables/marketing/02-seo/. Read the ledger product_context first;
  invent no keyword volumes or hypothetical catalog combinations. Not
  for a one-off SEO audit, AI citation reports, schema markup alone,
  copy drafts, or phase navigation.
---

# 程序化 SEO

根据真实目录维度和 SERP 证据，设计可落地的批量页面矩阵，写到 `deliverables/marketing/02-seo/`。缺证据就写缺口，不编造搜索量或虚构 SKU 组合。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）。把 `~` 展开为用户主目录，不要把 `~` 当相对路径。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/` 与 `deliverables/marketing/02-seo/` 里相关文件。列出：真实变体范围、询盘最多的市场、公司所在地、目标站点技术栈与 URL/模板约束、必须保留的已有页面。完成：能指出品类、市场、目录维度各依据哪几条；原文不拷进本仓库。品类、市场或技术栈缺到无法设计矩阵则停并写缺口，不编造组合、搜索量或竞品 URL。
3. **收集**。用网页搜索查证品类 × 应用 / 地点 / 对比 / 批发意图的公开 SERP；需要原文时抓取指定 URL 的正文。默认先搜再抓；搜索不可用则停止并写缺口。多页抓取需要隔离时 dispatch a subagent, else do it inline。查询意图、数据下限与核验：读 `references/methodology.md`。完成：每条声明有 URL、访问日期、摘录；变体矩阵来自实际目录；至少 3 个竞品程序化页面有可访问 URL，否则在缺口写明。
4. **分析**。按数据选页面类型，不要按习惯铺全类型。为每种类型写 URL 模式、变量来源、独特性方法、目标站点技术栈上的模板与批量路径、hub-and-spoke 内链、index / `noindex` 分层。先每类手工 1 个样本页的质量标准，再规划批次。页面优先级、变量库与独特性规则见 `references/methodology.md`。完成：至少 4 种页面类型有 URL 模式；同类型任意两页能指出至少三处实质差异；薄组合有合并或 `noindex` 策略。
5. **落盘**。写入下方路径与模板。策略与分析用简体中文；面客 URL、字段名、文件名按产品上下文语种（默认英文文件名）。工作簿可从 `templates/pseo-page-matrix.xlsx` 复制后填行；需要隔离时 dispatch a subagent, else do it inline。完成：主文档与工作簿非空；Page Matrix ≥50 行且每行 `source` 非空；教学支架原文零出现。

## 默认

- 本 skill 产出进 `deliverables/marketing/02-seo/`。不要用它做单页 SEO 审计、AI 引用报告或单独的结构化数据方案。
- 数字、搜索量、排名只来自：产品上下文、用户本轮提供、已搜索或已抓取的公开页、或上游 SEO 表。禁止估计后写成事实。
- 页面组合必须来自实际目录，不允许用假设维度生成。
- 目标渠道与目标站点技术栈以产品上下文为准，不在本文件写死平台。
- 100 个带真实规格、照片和询盘入口的页面，优于数千个薄变体。
- 表格式交付物每行有 `source`。终稿禁止占位 URL、禁止未替换的目录占位符。

## 写法

- 产品×属性页：真实规格、公差、项目照片、用途说明。
- 地点页：该市场的贸易条款、进口要点、本地项目或询盘证据、市场 FAQ；不要只改地名。
- 应用页：行业背景、典型用量、相关认证、推荐变体。
- 对比页：并排数据表，含使用周期成本、维护、安装差异。
- URL：小写、连字符、关键词可读，禁止仅 ID 的 slug。
- 有真实照片和规格的建议 index；薄组合 `noindex` 或合并，站点地图分段。

## 产出

路径：

- `deliverables/marketing/02-seo/programmatic-seo.md`
- `deliverables/marketing/02-seo/pseo-page-matrix.xlsx`（从 `templates/pseo-page-matrix.xlsx` 复制；列见 `references/methodology.md`）
- 同目录附件：`page-templates.md`、`data-matrix.md`、`url-structure.md`、`internal-linking-map.md`、`content-variables.md`

```markdown
# 程序化 SEO 策略

- source: 台账 product_context（不粘贴原文）
- accessed:
- stack:
- catalog_scope:

## 现状诊断

## 批量页面矩阵

## 优先批次建议

## 平台实施方案

## 内容独特性策略

## 内部链接架构

## Indexation 策略

## 可验证断言

## 下一步
```

每种页面类型必须写出：URL 模式、估计页数、主关键词模板、变量数据来源、独特性方法。工作簿至少含 Page Matrix、Variable Database、Implementation Plan 三张表，每行 `source` 非空。

## 例子

> 仅供理解，禁止引用到输出。

输入是实际目录里的品类、类型与在售品牌。成稿把页面类型收成「品类 hub × 类型切片 × 目录里实际出现的品牌切片」；应用/工况只做筛选，或少数带 SERP 证据的应用页。slug 与 H1 用该市场行业词。不是用自造品类词当 URL，不是把竞品主导航整棵复制成空文件夹，也不是品类×应用×地点×品牌无证据笛卡尔积。

输入是同一货架要做多市场页。成稿每个市场用该市场货架上的品类名词写 slug 与标题，地点页写该市场的贸易条款与询盘门槛；德制度名留在德页，美式电网词不写进欧页。不是把德语 slug 机翻成一个英文 umbrella 再套到各站，或只改地名与 hreflang。

应用页不要只把场景名换进去。交付物写该行业的典型用量、相关认证、推荐变体，并带来源；不写「本页专为该场景打造的一站式解决方案」，也不把本节句子粘进交付物。

## 易错

- 没读产品上下文就按通用矩阵开写。
- 用假设维度生成组合，或虚构搜索量。
- 只替换变量当内容，造成近重复。
- 先批量铺页再补内容。
- 忽略目标站点技术栈的 slug、层级或模板上限。
- 地点页只改地名，不写贸易条款与本地证据。
- 对比页没有并排数据表。
- 全部页面统一 index。
- 变量库 `source` 为空。
- 把教学例子或他站原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 变体矩阵来自实际目录；Page Matrix ≥50 行，每行有关键词证据与 `source`
- [ ] ≥3 个竞品程序化页面分析引用真实 URL
- [ ] 变量库覆盖目录实际维度（材质、表面、应用、地点等，以上下文为准）
- [ ] 每类页面有模板名、动态字段、批量创建方法
- [ ] 独特性策略按页面类型写清，不是「替换变量」
- [ ] 内链有 hub 与 spoke；index / `noindex` 与站点地图分段已写
- [ ] 产出在 `deliverables/marketing/02-seo/`；终稿无占位 URL
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
