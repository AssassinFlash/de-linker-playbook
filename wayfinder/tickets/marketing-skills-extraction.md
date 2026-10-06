---
wayfinder: task
status: closed
assignee: chesterjohn+agent
blocked_by: [extraction-spec, repo-skeleton]
resolved: 2026-10-06
---

# 38 个 marketing skill 抽取改写

## Question

从 `~/Documents/marketing-playbook-v3/.claude/skills/`（canonical，38 个；root `skills/` 是 legacy 不用）按抽取规格迁入本仓库 `skills/`，保持 `marketing-*` 命名。

执行方式：子代理 swarm，每 skill 一个子代理；按主题分批出 review checkpoint（编排系/基础/SEO/内容/获客/CRO/增长度量）；主模型按验收清单 review，不亲自改写。

注意：跳过 `.claude/product-profile.md`（不锈钢草稿）与任何数据文件；references/ 随各 skill 一并按规格处理。

资产已就位（assets-migration 票，2026-10-06）：Excel 空模板在 `templates/`，导出脚本在 `templates/scripts/`（v3 的 `scripts/build_excel.py` 与 `scripts/common/excel_writer.py` **未迁**）。源 skill 若写「用 build_excel.py 生成 Excel」，改写为能力描述 + 指向 `templates/` 与 `templates/scripts/to_excel.py`；填写 xlsx 依赖本机装 openpyxl。

## Resolution

38 个 marketing skill 全部按 `wayfinder/extraction-spec.md` 抽取完成（2026-10-06，一个会话，六批 swarm，每 skill 一个子代理，主模型只做组织与 checkpoint review）：

- 编排系 9（orchestrator/init/profile/product-profile/playbook-standards/teach/eval/evolve/skill-eval）；基础 7（foundation/psychology/positioning/pricing-strategy/launch-strategy/competitor-intelligence/copy-editing）；SEO 5（seo/ai-seo/seo-audit/site-and-schema/programmatic-seo）；内容 5（content/content-strategy/social-content/visual-content/copywriting 覆盖试点薄片）；获客 4（acquisition/email-outreach/inquiry-flow/paid-advertising）；CRO/增长度量 8（cro/funnel-optimization/landing-page/referral-program/retention/growth/measurement/analytics-and-optimization）。
- 每个 skill：`skills/<name>/SKILL.md`（frontmatter 只 name+description，description 300–700 字符）+ 按需 `references/`（>100 行均有目录）+ `.agents/skills/<name>` 相对软链。源 `evals/`、`AGENTS.md` 未迁；`marketing-orchestrator/references/dependency-graph.md` 由源 1016 行改写为 455 行本仓库形态。
- 验收清单 §8 十条全绿：name 正则/目录一致、description 区间、无禁用 frontmatter、无 harness 工具 ID（orchestrator 含固定子代理句）、禁止词零命中、例子标注齐、仓外路径仅 `~/Documents/New`、行数 <500、扁平+软链、无 `{{VAULT}}`/`vault_path`。
- 当轮修复 1 处：copy-editing 产出目录由子代理误入 `01-foundation/`，按 §7 机械映射改回 `03-content/copy-editing/`。
- 子代理集中偏离（有意、符合规格）：阶段包不再 delegate 回编排器（防循环）；源不存在的 `build_excel.py` 改为复制 `templates/*.xlsx` 或同目录 JSON；五引擎检索链统一收成「用网页搜索查证 / 抓取指定 URL」。
