---
wayfinder: prototype
status: closed
assignee: kimi（2026-10-10 认领）
resolved: 2026-10-10
blocked_by: [marketing-skills-extraction, lead-skills-extraction, review-fixes]
---

# 重叠 skill 对裁定合并

## Question

两源重叠约 5–6 对，逐对裁定：合并 / 并存分工 / 删一。疑似对（执行时以实际扫描为准）：

- `competitor-intelligence` ↔ `lead-competitor-analysis`
- `marketing-psychology` ↔ `lead-buyer-psychology`
- `email-outreach`（v3） ↔ `lead-cold-email-gen` / `lead-email-sequence-strategy`
- `marketing-seo` / `content-strategy` ↔ `lead-seo-editorial-guidelines` / `lead-seo-outline-gen` / `lead-seo-content-gen` / `lead-seo-content-edit`
- `positioning` / `marketing-foundation` ↔ `lead-usp-extraction`

形态：子代理逐对出对比提案（各自侧重、重复度、合并建议），主模型整理，用户裁定。裁定结果回写 skill 本体。

## Resolution

2026-10-10 走完：全量正文扫描定清单 → 11 对逐对出提案卡 → 用户裁定「**11 对全部并存分工**，优化点一并修复」→ 8 批子代理回写 + 5 处 references 清账。无一对合并或删一——共同理由：两树的编排硬依赖、交付根目录、粒度已分叉，硬合并会拆管线。落法统一为**收窄 description 触发词 + 正文互指/边界句**。验收：`evals/quick_validate.py` 81/81 全绿、`evals/validate_project.py` 退出码 0、主模型抽查 diff 通过。

### 逐对裁定与分工边界（均为并存分工）

1. **竞品**：`marketing-competitor-intelligence` = 厂对厂作战包（战斗卡/渠道价/vs 页）；`lead-competitor-analysis` = 利基策略地图×ICP 空白。description 按意图分流，双方互指。
2. **定位↔USP**：`marketing-positioning` = 产品级定位句+信息支柱；`lead-usp-extraction` = 相对竞品的可外发 USP/证据包。USP 输入步读 `product-positioning.md` 且不得矛盾。
3. **定位↔ICP**：`marketing-positioning` 停在角色级承诺；`lead-icp-analysis` 管分行业 ICP×四维外展策略。互指双向（已有对方产出则复用，不重切）。
4. **USP 内嵌竞品**：`lead-usp-extraction` 步骤 3 复用已核验竞品名单（marketing 01-foundation 或 lead 04-market），只补七轴 UVP，不从零找 15 家。
5. **邮件组**：`marketing-email-outreach` = 名单研究+角色模板库+生命周期培育（样品后/订单后/展会）；`lead-cold-email-gen`/`lead-followup-sequence`/`lead-email-sequence-strategy` = ICP×USP 成稿/九策跟进/编排；`lead-warm-email-transform` 暖化优先级以 sequence-strategy 为准。顺带修正票面遗漏：followup 在组内，`marketing-seo` 是阶段包不进对。
6. **内容↔SEO 四件套**：`marketing-content-strategy` 管「写什么/何时/哪集群」止于 brief；lead 四件套管「这一篇怎么写成 SEO 文」。outline-gen 软读营销日历/集群。
7. **心理**：`marketing-psychology` = 漏斗失速诊断+原则选型（description 去掉「买家心理」）；`lead-buyer-psychology` = 九场景共情→话术；价格异议 SOP 以 `lead-service-objection` 为准。
8. **教学器**：`marketing-teach` 只教 `marketing-*`（步骤 1 删「或 lead-*」）；`lead-teach` 只教 `lead-*`。互指双向。
9. **社媒**：`marketing-social-content` = 多平台战役日历（description 去掉「LinkedIn posts」成稿触发）；`lead-linkedin-topic-research`+10 帖类型 = 选题卡+单帖 Structure 成稿（topic-research 去掉「content calendar」）。帖类型 10 个「默认」节各加反向互指；`send_status`→`publish_status` 随多数统一（全仓 grep 无编排/模板/evals 引用）。Structure 编号不连续属外部课程体系，不重编。
10. **留存**：`marketing-retention` = 组合健康度/流失预警/沉默挽回（description 去 referral/commission，转介绍章收成推荐日志骨架、指向 `marketing-referral-program`）；`lead-service-retention` = 单买家交付后忠诚阶梯。
11. **编辑**：`marketing-copy-editing` = 转化文案七轮说服力审计；`lead-seo-content-edit` = SEO 成稿四操作八点编辑。互指对称。

### 优化点修复（用户裁定一并修）

- `lead-usp-extraction`：七步 vs 9 步编号对齐（步骤 2–8 = 七步管线）；步骤 8 冷邮件越界改指 `lead-cold-email-gen`；`usp-matrix` 统一 xlsx（写不了则 csv）；TAM/CAGR/HHI 补防诱编纪律。
- `marketing-email-outreach`：产出路径对齐到 `04-acquisition/email-outreach/`（含 references/methodology 与 orchestrator 依赖图 JSON）；「≥4 触点适用全部五条序列」写清；主题行 2–4 词软化为默认建议（A/B 可突破）。
- `marketing-psychology`：checklist「四段各≥1」与「只留 3–5 条」矛盾改清（总量 3–5，优先失速段）。
- 两个 teach：Stage 3 隔离用户稿、Stage 4 才评分读两份（`lead-teach` 矛盾厘清）；`lead-teach` 删「尚未迁入」过时表述；`marketing-teach` 补 learning-state 跨会话续读。
- `marketing-copy-editing`：≥10 行断言与「不为凑条数」统一为「目标，质量优先，不足不凑」。
- `lead-seo-content-gen`/`lead-seo-content-edit`：外链 ≥5 软化防凑数；硬/软依赖口径写清。
- `marketing-retention`：例子「90 天无联系」对齐 methodology「沉默≥6 个月」（methodology 同步修）。
- references 清账 5 处：usp `seven-step-pipeline.md` 步骤 7 去冷邮件、CI `methodology.md` 对比页只到纲要、orchestrator `dependency-graph.md` 的 email-outreach 路径、lead-teach `skill-teaching-guide.md` 去「尚未迁入」、retention `methodology.md` 沉默口径+转介绍收窄。

### 排除项（扫描后判定不重叠，不进裁定）

`marketing-seo`/`marketing-foundation`/`marketing-acquisition`/`marketing-orchestrator`（阶段包与双导航器，编排引用不算重叠）、`marketing-referral-program`↔`lead-service-retention`（佣金协议 vs 忠诚阶梯）、`marketing-copywriting`↔cold-email/seo-content-gen（转化文案库，粒度不同）、`marketing-seo-audit`↔`lead-search-term-expansion`/SEO 四件套（审计 vs 找词/成稿）、`marketing-content-strategy`↔`lead-linkedin-topic-research`（日历 vs 话题卡）、`lead-market-analysis`↔`marketing-positioning`、`marketing-pricing-strategy`↔`lead-service-quotation`、`marketing-inquiry-flow`↔`lead-service-first-contact`、`lead-targeted-outreach`↔`marketing-email-outreach`（单家定向 vs 批量模板）、`lead-magnet-gen`、`lead-product-knowledge`、`marketing-visual-content`↔`lead-linkedin-behind-scenes`、站点 CRO 三件套↔获客销售链、双方各自独有 skill。

### 同源重叠附注（不在本票范围，留作后续线索）

- `marketing-profile` ↔ `marketing-product-profile`：都是十五节覆盖索引，产出分别为 context-pointer / product-profile-index。
- `marketing-eval` ↔ `marketing-skill-eval`：验收清单 vs 八维定性（已互指）。
- `marketing-retention` 原内含转介绍章 ↔ `marketing-referral-program`（本票已顺手清：retention 只留日志骨架）。
- `marketing-landing-page` / `funnel-optimization` / `inquiry-flow`：description 触发词互吞。
- `marketing-copywriting` 的邮件/社媒片段 ↔ 同树 `email-outreach` / `social-content`。
- 获客侧竞品三套：`lead-competitor-analysis`、`lead-usp-extraction` 步骤 3–5、USP 买家卡 vs `lead-icp-analysis` 步骤 2（本票已用复用规则缓解）。
- 10 个 `lead-linkedin-*` 帖类型间靠 Structure 编号互斥，属拆分不是重叠。
