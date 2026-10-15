# 获客编排协议

编排器在每个方法 skill 落地前后读本文件：一份交付物从依赖检查到写入、再到下游过期的全过程。每次「下一步」怎么读反馈、挑动作在 `skills/lead-generation/SKILL.md`；反馈规则在 `docs/feedback-rules.md`。台账自驱动；打开 `skills/<name>/SKILL.md` 按其步骤做。不要用斜杠命令当入口。

## 目录

- [步骤 0 读配置与上下文](#步骤-0-读配置与上下文)
- [步骤 1 依赖检查](#步骤-1-依赖检查)
- [步骤 2 意图确认](#步骤-2-意图确认)
- [步骤 3 执行方法 skill](#步骤-3-执行方法-skill)
- [步骤 4 数据验证](#步骤-4-数据验证)
- [步骤 5 六维审查](#步骤-5-六维审查)
- [步骤 6 证据闸](#步骤-6-证据闸)
- [步骤 7 写入与过期](#步骤-7-写入与过期)
- [教学](#教学)
- [发现状态](#发现状态)

## 步骤 0 读配置与上下文

1. 读 `state/lead-status.md`，取出 `phase`、`next`、`method_skill`、`output_dir`、`product_context`。
2. 产品上下文：台账 `product_context`（事实源入口 `docs/fact-sources.md`），按其指路取证。入口读不到 → 停并写缺口，打开 `skills/marketing-profile/SKILL.md`（存在时）。原文不拷进本仓库。
3. 台账或 `deliverables/lead/` 缺失 → 打开 `skills/marketing-init/SKILL.md`。不要写项目根配置文件，不要另建产出根。
4. 若 `deliverables/lead/00-system/discovery-state.md`（或 `.json`）存在：把 `next_experiments.search_terms_to_try` 交给本轮方法 skill；不要把教学习作传进生产步骤。

## 步骤 1 依赖检查

1. 读 `references/dependency-graph.md`。
2. 取当前 skill 的硬依赖、软依赖。
3. 硬依赖：对应交付物 frontmatter `status` 为 `approved`（已过证据闸，见步骤 6）。
4. `ANY(a, b, c)`：至少一个为 `approved` 即通过。
5. 软依赖：标记可用/不可用，不阻塞。

硬依赖未满足且无 `user_waiver`：列出缺失项与应对方法 skill，阻塞。软依赖未就绪：列出后继续。

## 步骤 2 意图确认

产品上下文 + 已批准上游仍不够清楚时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）。预评分已够或用户说跳过 → 直接编译一段简短 Interview Context 交给步骤 3。该文件不存在 → 把缺口写入台账，不自造访谈。

Interview Context 只含已确认事实、偏好与约束，不含教学内容或用户习作。

## 步骤 3 执行方法 skill

打开 `skills/<method_skill>/SKILL.md` 并按其步骤做。需要隔离时 dispatch a subagent, else do it inline。单文件、无并行机会的工作 inline 做完。

执行时必须遵守 `references/search-protocol.md`：真实查证，搜索日志写进交付物末尾。搜索不足 → 报告实际数量，不得用训练数据填空白。

阻塞时引用 `references/manual-intervention-protocol.md` 的标准话术。

## 步骤 4 数据验证

优先打开 `skills/lead-data-validation/SKILL.md`。不存在则在本会话按下列五项做，标记结果、不删除数据。

| 验证项 | 做法 |
| --- | --- |
| URL 可访问性 | 抓取指定 URL，记录状态 |
| 公司真实性 | 用网页搜索交叉验证 |
| 域名匹配 | 名称/品类与域名一致；不确定再搜索 |
| 联系人真实性 | 用网页搜索查证公开职业页；未配置发现服务则标「联系人待补」 |
| 员工数 | 声称 vs 公开资料；缺则标缺口 |

同域名缓存；优先验证高 ICP 匹配；每 10 条报告进度。

## 步骤 5 六维审查

对交付物打六维。每维 PASS(100) / CONCERN(60) / FAIL(0)。综合分 = 六维平均（四舍五入）。`dependency-graph.md` 里该 skill 的 `review_checkpoints` 必须逐条 ✅/❌；任一 ❌ 至少降为 CONCERN。

| 维度 | 审查重点 |
| --- | --- |
| Completeness | 行数、必填字段、必填章节 |
| Data Accuracy | URL 可达、公司真实、联系人可验证或已标待补、有 data_source；有搜索日志 |
| Market Relevance | 匹配 ICP、地域/行业/规模在范围内 |
| Actionability | 足够发邮件或打电话，或已标明缺口；策略具体 |
| Differentiation | 覆盖不同子行业/地域，非同类重复 |
| Export Readiness | snake_case 列名、格式统一 |

决策：任一 FAIL → 重跑（回到步骤 3）；2 个及以上 CONCERN → 调整后重审；至多 1 个 CONCERN → 审查通过，那一项写进 `review_concerns`。审查通过不等于可以交出去，接着过步骤 6。

搜索日志缺失 → Data Accuracy 直接 FAIL。有阻塞无阻塞日志 → Actionability 至少 CONCERN。

自动修补不超过 3 轮，其后把决策交还操作者（修还是记 `user_waiver`）。

## 步骤 6 证据闸

六维审查通过后，AI 按 `docs/feedback-rules.md` 第 9 节逐条自查，在交付物末尾写 `## 证据闸` 一节，每条打 ✅ 或 ❌ 并写一句依据。不问操作者「行不行」：操作者只决定发不发、上不上，不审「写得好不好」，也不需要懂行业。

- 全部 ✅：frontmatter 写 `status: approved` 和 `evidence_gate: <日期>`。`approved` 的意思就是「已过证据闸」，和营销线同一个意思，由 AI 自查后写。
- 有 ❌：修一轮再查。还不过：`status` 留 `draft`，告诉操作者哪一条没过、为什么，编排换下一个动作。操作者明确接受某一条没过 → 记台账「豁免」表，再写 `approved`。
- 外展邮件、LinkedIn 帖、SEO 正文这类要发出去的文字，第 9 节第 3、4 条（说法可追到事实源、〔未证实〕不进对外文字）逐句查。

## 步骤 7 写入与过期

按 `references/write-protocol.md` 写入 `deliverables/lead/<阶段>/`。Markdown frontmatter：

```yaml
---
skill: lead-icp-analysis
product_context: ledger key only
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: approved
evidence_gate: YYYY-MM-DD
review_date: YYYY-MM-DD
review_score: 0
review_dimensions:
  completeness: PASS
  data_accuracy: PASS
  market_relevance: PASS
  actionability: PASS
  differentiation: PASS
  export_readiness: PASS
review_concerns: []
reviewer_recommendation: approve
review_history: []
upstream_versions: {}
stale_reason: ""
stale_date: ""
stale_confirmed: false
---
```

`status` 取值（和营销线同一套）：

| status | 意思 |
| --- | --- |
| `approved` | 六维审查通过，且已过证据闸；必须同时有 `evidence_gate` 日期 |
| `draft` | 文件在，还没过审查或证据闸 |
| `stale` | 曾是 `approved`，上游重写后过期；重过步骤 5、6 才回到 `approved` |
| `missing` | 文件不在（只在台账索引里用） |

不要写斜杠命令字段，不要粘贴产品原文。

表与文档同目录。重跑时旧版进 `deliverables/lead/99-archive/`。

写入后：按依赖图找出直接与间接下游；已 `approved` 的改为 `stale`，写上 `stale_reason` 与 `stale_date`（`evidence_gate` 保留，表示上次过闸是哪天）。回写 `state/lead-status.md`：改「审批与过期」表里本交付物与被标 `stale` 的下游各行；phase 边界再改 YAML、「当前」与「已完成」。不要另生成仓外仪表盘。

## 教学

教学走 `skills/lead-teach/SKILL.md`。产出进 `deliverables/lead/00-system/`，不改战役 `phase`。生产步骤不读取用户习作、教学内容或评分反馈。操作者说「跳过学习」则直接走步骤 0–7。

## 发现状态

若 `deliverables/lead/00-system/discovery-state.md` 存在：从搜索日志更新观察值（规则见 `discovery-state-schema.md`）。每 3 个 cycle 更新 `models` 与 `next_experiments`：需要隔离时 dispatch a subagent, else do it inline。不存在该文件则跳过。
