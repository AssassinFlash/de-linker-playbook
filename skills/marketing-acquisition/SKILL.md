---
name: marketing-acquisition
description: >
  Use when the user wants to build acquisition channels, run Phase 4
  Acquisition, 获客, 获客阶段, 社媒内容, 付费广告, 开发信, 冷邮件, 邮件序列,
  制定社媒内容计划, 帮我写开发信, 我要跑付费广告, 先跑一遍 acquisition
  阶段, or a full acquisition pass that needs social content, paid
  advertising, and email outreach together. Coordinate
  marketing-social-content, marketing-paid-advertising, and
  marketing-email-outreach from the product context named in the
  ledger; enforce hard dependencies before each method; write
  strategy docs and matching tables under
  deliverables/marketing/04-acquisition/. Not for a single ad
  campaign, email-sequence-only work, organic calendar only,
  product-profile setup, or phase navigation.
---

# 营销获客阶段

在产品上下文可读的前提下，按依赖把社媒内容、付费广告、邮件外展三个方法 skill 跑完。产出只进 `deliverables/marketing/04-acquisition/`。方法正文在那三个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。读 `state/marketing-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 acquisition 段与机器可读 JSON，核对 `global_gates`、三个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。三个方法的硬依赖（社媒：内容策略与定位；付费广告：定位、竞品与定价；邮件外展：定位与竞品）缺失且无 `user_waiver` → 停。三个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、三文件存在、三个方法各自的硬依赖。
3. **社媒、付费广告、邮件外展**。三者互无硬依赖，可并行：打开 `skills/marketing-social-content/SKILL.md`、`skills/marketing-paid-advertising/SKILL.md` 与 `skills/marketing-email-outreach/SKILL.md`，各 dispatch a subagent, else do it inline。完成：下方六件均在 `deliverables/marketing/04-acquisition/`（社媒与邮件在对应子目录）、非空、不是例子原文；三类交付物能回溯同一套定位与价值主张，卖点与 CTA 不互相矛盾。
4. **收束**。回写 `state/marketing-status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/04-acquisition/`）。当众列出六件交付物的本仓库相对路径，并给至少一项下一步。某方法失败、降级或因业务跳过时，总结写明阻塞点、影响范围及补救路径，不静默跳过。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、语气与价值主张陈述。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与平台名单以产品上下文为准，不预设某一电商、广告或社交平台。
- 查证由方法 skill 做：用网页搜索查证；需要原文时抓取指定 URL 的正文。缺搜索则停并写缺口，不编造。
- 联系人/邮箱发现服务仅当用户已配置；否则交付物标「联系人待补」。外发工具仅当用户已配置才发信；未配置则只产出文案不发送。
- 三者互无硬依赖，可并行；单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/04-acquisition/social-content/` | `deliverables/marketing/04-acquisition/social-content/social-calendar.xlsx` |
| `deliverables/marketing/04-acquisition/paid-advertising.md` | `deliverables/marketing/04-acquisition/paid-advertising-blueprint.xlsx` |
| `deliverables/marketing/04-acquisition/email-outreach/` | `deliverables/marketing/04-acquisition/email-outreach/prospect-research.xlsx` |

按方法 skill 另有则一并核：`sequence-builder.xlsx`（与邮件外展同目录）。目录产出：对应子目录下至少 1 个非空 `.md`。

宣布：

```markdown
- phase: 4
- phase_name: 获客
- method_skill: marketing-acquisition
- output_dir: deliverables/marketing/04-acquisition/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「买家看不见净价，先跑一遍 acquisition」。上下文可读，三个方法 skill 都在，上游硬依赖已满足。三者并行：社媒日历、付费广告蓝图、开发信与名单一起落盘。总结列出六条本仓库相对路径，不把本节句子写入交付物，也不发信。

用户说「EPC 是商业谈判和技术批准两道闸，先跑获客阶段」。同样宣布 phase 4、`marketing-acquisition` 与 `deliverables/marketing/04-acquisition/`，不在本层写选题、关键词或开发信。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做社媒、付费广告或邮件外展。
- 方法 skill 不存在时自造社媒、广告或开发信步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表。
- 只跑其中一个方法却宣称本阶段完成。
- 社媒、广告、邮件的卖点或 CTA 互相矛盾。
- 未配置外发工具却发送；未配置联系人发现却编造邮箱。
- 写仓外运行日志，或把执行细节只写进 Markdown、把策略说明只塞进表。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 三个方法 skill 都已按其正文跑完，未自造流程
- [ ] 六件交付物在 `deliverables/marketing/04-acquisition/`，非空，不是例子原文
- [ ] 三类交付物定位与 CTA 一致；未配置则不发送、联系人待补
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
