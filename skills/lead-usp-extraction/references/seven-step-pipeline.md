# 七步差异化管线

条件：跑 USP 提炼且需要逐步字段、交付物标题或重跑规则时读本文。执行顺序与完成条件以 `SKILL.md` 为准。

## 目录

- [总览](#总览)
- [步骤 1 利基与买家](#步骤-1-利基与买家)
- [步骤 2 竞品盘点](#步骤-2-竞品盘点)
- [步骤 3 UVP 挖掘](#步骤-3-uvp-挖掘)
- [步骤 4 Gap 矩阵](#步骤-4-gap-矩阵)
- [步骤 5 能力叠加](#步骤-5-能力叠加)
- [步骤 6 差异化方案](#步骤-6-差异化方案)
- [步骤 7 定位与内容](#步骤-7-定位与内容)
- [USP-ICP 匹配](#usp-icp-匹配)
- [跨步依赖](#跨步依赖)
- [重跑](#重跑)

## 总览

```
利基与买家 → 竞品盘点 → UVP 挖掘 → Gap 矩阵
     → 能力叠加 → 差异化方案 → 定位与内容 → USP-ICP 匹配
```

逐步交接：上一步的指定交付物是下一步的输入。步骤 1 的买家卡片在步骤 7 再次使用。

## 步骤 1 利基与买家

**输入：** 可做菜单 3–6 项、出口区域、暂定买家角色。

**规则：** 最多两问。有来源的进入容易度 <60 或 CAGR <5% 不推荐。产品上下文已锁定的利基只记分数、不拒绝。无来源的 TAM/CAGR 写「未在来源出现」，不以缺失 CAGR 当作 <5%。进入容易度必须有一句依据。

**交付物标题（一字不改）：**

1. Short-List of Micro-Niches — 表：Niche | TAM | 3-yr CAGR % | Top Demand Drivers | Ease-of-Entry /100 | Fatal Drawback。表后一句理由。
2. Recommended Niche (Deep Dive) — Market Dynamics（规模、增长催化、监管）; Value-Chain Map（原料到终端）; Entry Barriers & How We Overcome Them。
3. Buyer Persona Card — Job Title, Typical KPIs, Daily Workflow, Pain Points, Buying Triggers, Deal-breakers。
4. No-Go Niches — 2–3 条 + 决定性红旗。

**交接：** 第 2–3 节进入步骤 2。

## 步骤 2 竞品盘点

**输入：** 步骤 1 的利基与买家。区域与步骤 1 相同。

**目标名单：** 15 家。默认营收档：大 >$500M、中 $50–500M、小 <$50M，各 5 家。营收取最近已披露财年并写年份。该利基没有足够可核验的大营收玩家、或公开营收不足时：改按该利基相对体量分在位者 / 挑战者 / 利基商，在表中注明分档依据；名单短于 15 就写缺口，不拿无关公司凑数。

**每家字段：** HQ；营收（或「未在来源出现」）；旗舰产品线；主渠道；最近战略动作（并购、资本开支、产品上市、可持续承诺）；官网。

**交付物：**

- A. Competitor Table — Company | Size Tier | HQ | Rev | Flagship Offer | Main Channels | Latest Strategic Move | Website
- B. Strategic Patterns Commentary（约 150 词）— 价格带 vs 溢价带、技术押注、动作里透出的未满足需求
- C. Competitive Intensity Gauge — 有份额才算 HHI；否则定性高/中/低并说明对后来者的含义

**交接：** 表 A 进入步骤 3。未核验域名的行不进入挖掘，或单独标 unverified。

## 步骤 3 UVP 挖掘

**输入：** 步骤 2 表 A 中已核验的公司。

**方法：** 用网页搜索查证官方域名；抓取首页与 About（或等价页）。需要评价、证书、年报时再搜，并抓取能打开的来源页。搜索或抓取不可用则停止并写缺口。

**每家采集：** 最多 4 条 UVP。Explicit Claim = 对方自己的话。Implied Proof = 评价、证书、案例。轴：Speed | Cost | Quality | Customization | Sustainability | Service | Digital Tool | Other。摘录 5–12 词或 URL 片段。

**交付物：** 公司分块列表；Cross-Competitor Heat-Map Summary（约 120 词）。

**交接：** 全部 UVP 块进入步骤 4。禁止用模型记忆补 UVP。

## 步骤 4 Gap 矩阵

**输入：** 步骤 3 的 UVP 集。

行=公司，列=七轴（不含 Other）。有 ≥1 条该轴 UVP 为 check，沉默为 —。过挤：≥70% 有 check。空白：≤30% 有 check。中性：31–69%。

空白轴必须对照步骤 1 买家痛点或 ICP；未提到的不记为机会。符号：check / —；过挤 ≥70%，空白 ≤30%，中性 31–69%。

**交付物：** Markdown 矩阵 + Over-Served Axes + Under-Served Axes / White-Spaces（合计约 150 词）。

**交接：** 矩阵 + 空白轴进入步骤 5，并附我方能力数字。

## 步骤 5 能力叠加

**输入：** 步骤 4 的矩阵与空白轴。我方硬数字（用户填，缺则 `?`）：交期（天）、MOQ、不良率（%）、证书、独特工艺、可持续资质。

**任务：**

1. 加「我方」行。
2. 符号：`double-check` 优于该轴领先者；`check` 跟上；`—` 无主张；`cross` 差于领先者 20% 以上；`?` 无数据。
3. 每个 `cross` 写瓶颈：人 / 设备 / 政策 / 供应链。
4. 空白轴里，与现有优势对齐或 ≤6 个月可达到的，标快赢。

**交付物：** Annotated Matrix；Diagnostic Commentary（Strengths / Exposed Weaknesses / Quick-Win White-Spaces）；Risk Note（强但易被抄的轴）。

**交接：** 快赢列表进入步骤 6。

## 步骤 6 差异化方案

**输入：** 步骤 5 的快赢。约束（用户填，缺则待补）：现金预算、工程工时、合规上限。不发明预算数字。

每个机会 3 个选项（服务承诺、技术附加、担保、内容资产、可持续角度等）。每项：

| 维 | 取值 |
| --- | --- |
| Buyer Impact | High / Medium / Low（拉动哪项 KPI） |
| Ease-of-Implementation | Easy / Moderate / Hard |
| Cost Band | $ / $$ / $$$ |
| Time-to-Market | ≤30 天 / 1–3 月 / 3–6 月 / >6 月 |
| Imitation Barrier | Thin / Moderate / High |

**交付物：** 机会表；Prioritised Short-List（Top-3）+ 为何第 1 优于 2–3；P0 必做 / P1 建议 / P2 可选。

**交接：** Top-3 进入步骤 7。

## 步骤 7 定位与内容

**输入：** 步骤 6 的 Top-3；步骤 1 的买家卡片。

1. One-Sentence Positioning Line — ≤14 词，主差异化 + 买家 KPI
2. Persuasion Layer-Cake — Hook → Pain Amplifier → Proof of Differentiator → Risk-Reversal → CTA
3. Proof-Kit Checklist — 指标截图、案例短故事、证书、省钱测算、45 秒产线视频、质保条款等，按说服力排序；每项标已有或待补
4. Consultative Cold Email — 主题 ≤8 词、无 emoji；正文 ≤120 词；微故事 + 一个证据；单一低压 CTA（开放问题或微承诺）。只产文案，不发送
5. 30-sec Talk-Track — 镜像句 → 校准问句（How would you ...）→ 有条件让步

面客文字用买家语言（缺省英语）。收束：先邮件块，再落地页块，再补证据包资产。有 30 天转化数据后从 Gap 矩阵重跑。

## USP-ICP 匹配

管线之后把每条 USP 映射到 ICP：

- 一封外发信一条主 USP
- 不同买家可对应不同 USP
- 4–6 条，类型用实际用到的：产品级（功能、耐久、性能）；运营（交期、MOQ、排产弹性）；信任（证书、质检、售后）；战略价值（上市速度、共创、可持续）
- 每条：Headline → Buyer Angle → Proof → 目标 ICP → Competitive Frame

## 跨步依赖

```
步骤 1 → 2 → 3 → 4 → 5 → 6 → 7 → 匹配
  │                              │
  └──────── 买家卡片 ────────────┘
```

## 重跑

- 30 天市场或转化反馈：从 Gap 矩阵重跑（SKILL 步骤 5 起）
- 新进入者或并购：从竞品盘点重跑（SKILL 步骤 3 起）
- 产品菜单变化：从利基与买家重跑（SKILL 步骤 2 起）
