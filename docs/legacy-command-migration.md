# 旧入口迁移说明

早期版本用斜杠命令卡片做入口。后来改为 **Skills**。本仓库的正典是 `skills/<name>/SKILL.md`（目录名 = frontmatter `name`），不再维护命令卡片或专家角色文件。用户打开对应 `SKILL.md` 并按其步骤做。

下表保留 v2 → 方法 skill 的对照，便于旧习惯检索。路径一律相对本仓库。无独立「阶段聚合」skill：阶段只决定 `deliverables/marketing/<phase>/` 或 `deliverables/lead/<phase>/` 的落点，由 `skills/marketing-orchestrator/SKILL.md` 按台账分派。

## 迁移总览

| 旧入口 | 现入口 | 说明 |
|---|---|---|
| `/marketing-init` | `skills/marketing-init/SKILL.md` | 项目初始化 |
| `/marketing-foundation` | 编排器 + 方法 skill；产出 `deliverables/marketing/01-foundation/` | 已无阶段聚合入口 |
| `/marketing-seo` | 编排器 + SEO 方法 skill；产出 `deliverables/marketing/02-seo/` | 已无阶段聚合入口 |
| `/marketing-content` | 编排器 + 内容方法 skill；产出 `deliverables/marketing/03-content/` | 已无阶段聚合入口 |
| `/marketing-acquisition` | 编排器 + 获客方法 skill；产出 `deliverables/marketing/04-acquisition/` | 已无阶段聚合入口 |
| `/marketing-cro` | 编排器 + CRO 方法 skill；产出 `deliverables/marketing/05-cro/` | 已无阶段聚合入口 |
| `/marketing-growth` | 编排器 + 增长方法 skill；产出 `deliverables/marketing/06-growth/` | 已无阶段聚合入口 |
| `/marketing-measurement` | 编排器 + 测量方法 skill；产出 `deliverables/marketing/07-measurement/` | 已无阶段聚合入口 |
| `/marketing-status` | `skills/marketing-orchestrator/SKILL.md` | 读台账汇报状态 |
| `/marketing-next` | `skills/marketing-orchestrator/SKILL.md` | 下一步建议 |
| `/marketing-profile` | `skills/marketing-profile/SKILL.md` | 产品上下文指路 |
| `/marketing-positioning` | `skills/marketing-positioning/SKILL.md` | 定位策略 |
| `/marketing-pricing` | `skills/marketing-pricing-strategy/SKILL.md` | 定价策略 |
| `/marketing-competitors` | `skills/marketing-competitor-intelligence/SKILL.md` | 竞品情报 |
| `/marketing-content-strategy` | `skills/marketing-content-strategy/SKILL.md` | 内容策略 |
| `/marketing-copywriting` | `skills/marketing-copywriting/SKILL.md` | 文案撰稿 |
| `/marketing-social` | `skills/marketing-social-content/SKILL.md` | 社媒内容 |
| `/marketing-seo-audit` | `skills/marketing-seo-audit/SKILL.md` | SEO 审计 |
| `/marketing-seo-ai` | `skills/marketing-ai-seo/SKILL.md` | AI SEO |
| `/marketing-seo-programmatic` | `skills/marketing-programmatic-seo/SKILL.md` | 程序化 SEO |
| `/marketing-site-arch` | `skills/marketing-site-and-schema/SKILL.md` | 网站架构 |
| `/marketing-schema` | `skills/marketing-site-and-schema/SKILL.md` | Schema 标记 |
| `/marketing-paid-ads` | `skills/marketing-paid-advertising/SKILL.md` | 付费广告 |
| `/marketing-ad-creative` | `skills/marketing-visual-content/SKILL.md` | 广告创意 |
| `/marketing-video-script` | `skills/marketing-visual-content/SKILL.md` | 视频脚本 |
| `/marketing-image-prompts` | `skills/marketing-visual-content/SKILL.md` | 图片生成提示词 |
| `/marketing-cold-email` | `skills/marketing-email-outreach/SKILL.md` | 冷邮件 |
| `/marketing-email-sequence` | `skills/marketing-email-outreach/SKILL.md` | 邮件序列 |
| `/marketing-page-cro` | `skills/marketing-landing-page/SKILL.md` | 着陆页 CRO |
| `/marketing-form-cro` | `skills/marketing-inquiry-flow/SKILL.md` | 表单/询盘流程 CRO |
| `/marketing-onboarding-cro` | `skills/marketing-funnel-optimization/SKILL.md` | 漏斗 CRO |
| `/marketing-launch` | `skills/marketing-launch-strategy/SKILL.md` | 上市策略 |
| `/marketing-referral` | `skills/marketing-referral-program/SKILL.md` | 推荐计划 |
| `/marketing-churn` | `skills/marketing-retention/SKILL.md` | 留存/复购 |
| `/marketing-analytics` | `skills/marketing-analytics-and-optimization/SKILL.md` | 数据分析体系 |
| `/marketing-revops` | `skills/marketing-analytics-and-optimization/SKILL.md` | 营收运营 |
| `/marketing-ab-test` | `skills/marketing-analytics-and-optimization/SKILL.md` | A/B 测试 |
| `/marketing-sales-enablement` | `skills/marketing-content-strategy/SKILL.md` | 销售赋能资料 |
| `/marketing-free-tool` | `skills/marketing-content-strategy/SKILL.md` | 免费工具 / Lead Magnet |
| `/marketing-ideas` | `skills/marketing-content-strategy/SKILL.md` 或 `skills/marketing-social-content/SKILL.md` | 内容创意 |
| `/marketing-interview` | `skills/marketing-product-profile/SKILL.md` | 客户访谈材料（产品侧） |
| `/marketing-eval` | `skills/marketing-eval/SKILL.md` | 评估与校验 |
| `/marketing-evolve` | `skills/marketing-evolve/SKILL.md` | Skill 迭代改进 |
| `/marketing-teach` | `skills/marketing-teach/SKILL.md` | 教学/解释 |
| `/marketing-paywall-cro` | 已删除 | 不适用于本 playbook 的 B2B 场景 |
| `/marketing-popup-cro` | 已删除 | 不适用于本 playbook 的 B2B 场景 |
| `/marketing-signup-cro` | 已删除 | 不适用于本 playbook 的 B2B 场景 |
| `/scraper` | 已删除 | 采集能力写在相关方法 skill 的步骤里 |

无前缀的旧 skill 名（如 `copywriting`、`product-profile`、`skill-eval`）在本仓库分别对应 `marketing-copywriting`、`marketing-product-profile`、`marketing-skill-eval`。

## 如何选择入口

1. **不知道从何开始**：读 `state/status.md`，打开 `skills/marketing-orchestrator/SKILL.md` 或 `skills/marketing-init/SKILL.md`。
2. **知道阶段、不知道具体任务**：仍走编排器；不要寻找 `/marketing-{phase}` 聚合入口。
3. **知道具体任务**：打开对应 `skills/<name>/SKILL.md`。
4. **需要隔离的重活**：方法 skill 会写 dispatch a subagent, else do it inline，不另点名一套专家角色文件。

## 已删除命令的处理

对于已删除的入口（`/marketing-paywall-cro`、`/marketing-popup-cro`、`/marketing-signup-cro`、`/scraper`）：

- 它们要么只适用于订阅制产品，要么已内置到其他方法 skill。
- 若确实需要这些能力，在对应 skill 中提出，或评估是否新增独立 skill。
