---
name: marketing-seo
description: >
  Use when the user wants to build or optimize SEO strategy, run Phase 2
  SEO, SEO 策略, 帮我审计网站 SEO, SEO 审计, 怎么做 AI 搜索可见性,
  AI SEO, 程序化 SEO, programmatic SEO, 网站架构与 schema, 先跑一遍
  seo 阶段, or a full SEO pass that needs audit, AI SEO, programmatic
  SEO, and site/schema together. Coordinate
  marketing-seo-audit, marketing-ai-seo, marketing-programmatic-seo, and
  marketing-site-and-schema from the product context named in the ledger;
  enforce hard dependencies before AI SEO, programmatic SEO, and
  site/schema; write strategy docs and matching tables under
  deliverables/marketing/02-seo/. Not for a single schema map,
  AI-visibility-only work, one content calendar, product-profile setup,
  or phase navigation.
---

# 营销 SEO 阶段

在产品上下文可读的前提下，按依赖把 SEO 审计、AI SEO、程序化 SEO、站点与 schema 四个方法 skill 跑完。产出只进 `deliverables/marketing/02-seo/`。方法正文在那四个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。入口读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 seo 段与机器可读 JSON，核对 `global_gates`、四个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。审计的硬依赖（定位、竞品）缺失且无 `user_waiver` → 停。四个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、四文件存在、审计的硬依赖。
3. **审计**。打开 `skills/marketing-seo-audit/SKILL.md`，dispatch a subagent, else do it inline。完成：`seo-audit.md` 与 `seo-audit-data.xlsx` 均在 `deliverables/marketing/02-seo/`、非空、不是例子原文。
4. **AI SEO 与程序化 SEO**。仅当步骤 3 交付物 frontmatter 为 `approved`，或台账已记 `user_waiver`。二者互无硬依赖，可并行：打开 `skills/marketing-ai-seo/SKILL.md` 与 `skills/marketing-programmatic-seo/SKILL.md`，各 dispatch a subagent, else do it inline。完成：下方四件均在同目录、非空、不是例子原文。
5. **站点与 schema**。仅当步骤 3 与步骤 4 的程序化 SEO 交付物 frontmatter 为 `approved`，或台账已记 `user_waiver`。打开 `skills/marketing-site-and-schema/SKILL.md`，dispatch a subagent, else do it inline。完成：`site-and-schema.md` 与 `site-schema-blueprint.xlsx` 同上目录、非空、不是例子原文。
6. **收束**。回写 `state/marketing-status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/02-seo/`）。当众列出八件交付物的本仓库相对路径，并给至少一项下一步。某方法失败或降级时，总结写明阻塞点、影响范围及补救路径。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、关键词与站点技术栈陈述。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与目标站点技术栈以产品上下文为准。
- 查证由方法 skill 做：用 Apify 搜索查证；需要原文时抓取指定 URL 的正文。Apify 与替代取证仍不可得则停并写缺口，不编造。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/02-seo/seo-audit.md` | `deliverables/marketing/02-seo/seo-audit-data.xlsx` |
| `deliverables/marketing/02-seo/ai-seo.md` | `deliverables/marketing/02-seo/ai-visibility-report.xlsx` |
| `deliverables/marketing/02-seo/programmatic-seo.md` | `deliverables/marketing/02-seo/pseo-page-matrix.xlsx` |
| `deliverables/marketing/02-seo/site-and-schema.md` | `deliverables/marketing/02-seo/site-schema-blueprint.xlsx` |

宣布：

```markdown
- phase: 2
- phase_name: SEO
- method_skill: marketing-seo
- output_dir: deliverables/marketing/02-seo/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「公开目录登录前买家看不见净价；安装商搜批发是地理优先、品牌加 Großhandel，兼容按逆变器品牌问 Freigabeliste，中间带对大厂太小、对本地电工太大。先跑一遍 seo 阶段」。上下文可读，四个方法 skill 都在。先做审计；审计批准后并行 AI SEO 与程序化 SEO；程序化批准后再做站点与 schema。总结列出八条本仓库相对路径，不把本节句子写入交付物。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做 AI SEO、程序化 SEO 或站点与 schema。
- 方法 skill 不存在时自造审计、AI SEO、程序化或 schema 步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表。
- 四个方法全部串行，未在审计批准后并行 AI SEO 与程序化 SEO。
- 只跑其中一个方法却宣称本阶段完成。
- 把子 skill 中间草稿当最终交付物。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 四个方法 skill 都已按其正文跑完，未自造流程
- [ ] 八件交付物在 `deliverables/marketing/02-seo/`，非空，不是例子原文
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
