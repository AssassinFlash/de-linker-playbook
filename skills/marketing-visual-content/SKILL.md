---
name: marketing-visual-content
description: >
  Use when the user asks for image prompts, AI images, video script, product
  video, social video, visual strategy, 配图方案, 视频脚本, 短视频, Midjourney
  prompt, Runway prompt, factory tour, product demo, visual content calendar,
  AI 生图, 视觉策略, or 视觉内容. Collect platform visual trends and competitor
  galleries, then write a visual strategy, prompt library, and shot-by-shot
  video scripts under deliverables/marketing/03-content/. Read the ledger
  product_context first; invent no view counts, engagement rates, or
  reference URLs. Not for drafting conversion copy, SEO audits, paid-media
  buying, caption calendars without visuals, or phase navigation.
---

# 视觉内容

为 B2B 外贸营销写出可执行的视觉策略、AI 生图提示词与视频脚本，落到 `deliverables/marketing/03-content/`。无来源的风格判断、无画幅的套图、纯文案日历，不走本文件。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/03-content/content-strategy.md` 与 `deliverables/marketing/01-foundation/` 定位相关交付物。完成：能指出品类、目标市场、品牌语气、应用场景各依据哪几条陈述；原文不拷进本仓库。缺项写成缺口清单；产品上下文不存在则停，不编造公司、产品或视觉规范。
3. **范围**。确认交付类型（静图 / 视频 / 二者）、目标渠道（以产品上下文为准）、画幅、时长、核心目标、资产模式（实拍 / 仅照片 / AI 生成 / 混合）、出镜对象、用户已配置的生图或生视频工具。完成：类型、渠道、资产模式各有一句可辩护理由。
4. **采集**。用网页搜索查证同品类视觉趋势、短视频钩子、竞品图库或频道；需要原文时抓取指定 URL 的正文（含动态页）。查询意图、平台画幅与最低条数见 `references/methodology.md`。多页抓取需要隔离时 dispatch a subagent, else do it inline。完成：每条证据有 URL、摘录、访问日期；搜索不可用则停止并写缺口，不编造浏览量、互动率或参考链接。
5. **分析**。归纳 3–5 个可复核的视觉风格、竞品缺口（缺失角度 / 场景 / 画幅）、以及（若做视频）3 个差异化钩子。按 `references/methodology.md` 写风格表、场景映射、提示词结构与逐镜字段。完成：每个风格有频次证据与来源；每个 prompt 能回溯至少一条已采集参考。
6. **落盘**。写入下方路径。完成：策略文档与工作簿非空；prompt 库 ≥10 条且均有 `source` 与画幅；竞品 ≥3 家；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客脚本、文件名、prompt 语种以产品上下文为准，同一段不混用。
- 目标渠道以产品上下文为准。未点名平台时，只覆盖上下文里的渠道，不默认某一电商或社交平台。
- 查证用网页搜索；需要原文时抓取指定 URL。不写工具 ID，不并列多引擎菜单。
- 生图 / 生视频工具以用户已配置者为准；未配置则只交 prompt 与脚本，不声称已出图或已成片。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 先有可核验参考，再写 prompt 或脚本。风格名必须能指回采集到的图或片，不套「高端大气」。
- 每条视觉建议同时写：目标渠道、画幅、参考 URL、频次或样本数。
- 静图 prompt 结构：主体 + 风格 + 机位 + 光线 + 场景 + 质量词 + 画幅。材质、表面、应用场景只写产品上下文已有的，缺则标「未在上下文出现」。
- 视频：先定目标对应的文案框架，再给 3 个钩子（写清前 3–5 秒），再写逐镜表（画面、旁白、运镜、灯光、音效、时长、来源）。品牌语气（权威 / 挑战 / 亲近）用产品上下文校准，并附一句样例台词。
- 给用户选择：同一用途至少 2 条 prompt 或 3 个钩子，不交单选项。
- 禁止在终稿留 `[insert image here]`、`[待补充]` 等未解释占位。

## 产出

路径：

- `deliverables/marketing/03-content/visual-content/index.md`
- `deliverables/marketing/03-content/visual-assets/prompt-library.md`
- `deliverables/marketing/03-content/visual-assets/video-scripts/`（仅当范围含视频）
- `deliverables/marketing/03-content/visual-style-guide.xlsx`（从 `templates/visual-style-guide.xlsx` 复制后填；无脚本则按列手写，不另造构建器）
- 按需同目录执行附件：规格见 `references/methodology.md`

```markdown
# 视觉内容策略

- source: 台账 product_context（不粘贴原文）
- asset_mode:
- platforms:
- accessed:

## 视觉趋势总览

## 竞品视觉/视频分析

## 平台视觉策略

## 生图/生视频工具选型

## Prompt / Script 库概览

## 行动建议（P0 / P1 / P2）

## 可验证断言
```

工作簿至少含 `prompt_library`、`visual_trends`、`video_scripts`、`competitor_audit`；每行必须有非空 `source`。未做视频时 `video_scripts` 写明「本轮不做视频」及原因，不留空表充数。

## 例子

> 仅供理解，禁止引用到输出。

输入写「案例页配图 + 客户证言人像」。成稿应改成指标、范围、边界三件套：画面只交代可核验的数量或投运状态、装了什么、角色分到哪里为止；图里没发生的事不画。没有已同意出镜的说话人就不生成人像、假签名或假证言条。公开制造商案例页常见事实块先于故事、无客户原话也能站住；施工未完的图标明进行中，不画成已投运。不要写「满意客户头像 + 工厂大门合影」。

输入写「产品主图 prompt」。先做当前线上图与拟替换的对照：已有图引用保留，只写拟替换的主体、中性背景、机位、光线和画幅，并带来源 URL。上下文没有自有产线或自有质保现场，就不画产线门头或质保柜台。不写无来源的「高端大气产品图」。

输入写「工厂参观短视频」。成稿应改成身份边界内的画面（配对核验、调试/质保协调、出货检查），钩子用范围或投运状态，不编造出镜采访。不拍自有产线或屋顶施工队。也不把本节句子粘进交付物。

## 易错

- 没读产品上下文就套通用视觉稿。
- 不采集真实趋势就写 prompt 或脚本。
- 忽略渠道画幅，用一个尺寸应付全部平台。
- 风格或钩子没有竞品或趋势来源。
- 编造浏览量、钉图数、互动率或参考 URL。
- 只给一条 prompt 或一个钩子。
- 品牌语气、框架、钩子未确认就写全片。
- 终稿残留未解释占位符，或把本节例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 类型、渠道、资产模式已写清；渠道匹配产品上下文
- [ ] 趋势参考、竞品图/帧、平台短视频样本达到 `references/methodology.md` 最低条数，或已写搜索缺口
- [ ] Top 风格有频次证据；竞品缺口指向具体角度/场景/画幅
- [ ] 每条 prompt 有画幅、工具、source；视频则有 3 个钩子与七字段逐镜表
- [ ] 主文档与工作簿在 `deliverables/marketing/03-content/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
