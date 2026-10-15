# 营销依赖图

编排器做闸门检查时读本文件。阶段目录小写；方法 skill 在 `skills/<name>/SKILL.md`；战役产出在 `deliverables/marketing/<阶段>/`。

## 目录

- [横切](#横切)
- [阶段](#阶段)
- [技能登记](#技能登记)
- [依赖边](#依赖边)
- [状态判定](#状态判定)
- [闸门](#闸门)
- [附属贡献](#附属贡献)
- [机器可读图](#机器可读图)

## 横切

- 每个方法 skill 依赖台账 `product_context`（事实源入口 `docs/fact-sources.md`）。读不到则停，打开 `skills/marketing-profile/SKILL.md`（文件存在时）。
- 共用规则：`skills/marketing-playbook-standards/SKILL.md`（存在则读）。
- 台账或 `deliverables/marketing/` 缺失：打开 `skills/marketing-init/SKILL.md`。
- 教学 / 评测 / 进化产出进 `deliverables/marketing/00-system/`，不占用战役 phase。

## 阶段

| 阶段目录 | 入口 skill（若已迁入，可选打包） | 方法 skill |
| --- | --- | --- |
| （phase 0，无目录） | `marketing-profile` | 只读产品上下文 |
| `00-research` | — | 调研摘录，回写下游表 |
| `00-system` | `marketing-teach`、`marketing-eval`、`marketing-evolve`、`marketing-skill-eval` | 元产出 |
| `01-foundation` | `marketing-foundation` | `marketing-positioning`、`marketing-competitor-intelligence`、`marketing-pricing-strategy` |
| `02-seo` | `marketing-seo` | `marketing-seo-audit`、`marketing-ai-seo`、`marketing-programmatic-seo`、`marketing-site-and-schema` |
| `03-content` | `marketing-content` | `marketing-content-strategy`、`marketing-copywriting`、`marketing-visual-content` |
| `04-acquisition` | `marketing-acquisition` | `marketing-social-content`、`marketing-paid-advertising`、`marketing-email-outreach` |
| `05-cro` | `marketing-cro` | `marketing-landing-page`、`marketing-inquiry-flow`、`marketing-funnel-optimization` |
| `06-growth` | `marketing-growth` | `marketing-launch-strategy`、`marketing-referral-program`、`marketing-retention` |
| `07-measurement` | `marketing-measurement` | `marketing-analytics-and-optimization` |

编排器默认直接打开方法 skill。入口 skill 存在且用户点名该阶段时，按其正文跑完该阶段方法 skill。

## 技能登记

路径均为本仓库相对路径。表文件与策略文档同目录。

| Skill | 策略文档 | 表 |
| --- | --- | --- |
| `marketing-positioning` | `deliverables/marketing/01-foundation/product-positioning.md` | `positioning-data.xlsx` |
| `marketing-competitor-intelligence` | `deliverables/marketing/01-foundation/competitor-analysis.md` | `competitor-profiles.xlsx` |
| `marketing-pricing-strategy` | `deliverables/marketing/01-foundation/pricing-strategy.md` | `pricing-benchmark.xlsx` |
| `marketing-seo-audit` | `deliverables/marketing/02-seo/seo-audit.md` | `seo-audit-data.xlsx` |
| `marketing-ai-seo` | `deliverables/marketing/02-seo/ai-seo.md` | `ai-visibility-report.xlsx` |
| `marketing-programmatic-seo` | `deliverables/marketing/02-seo/programmatic-seo.md` | `pseo-page-matrix.xlsx` |
| `marketing-site-and-schema` | `deliverables/marketing/02-seo/site-and-schema.md` | `site-schema-blueprint.xlsx` |
| `marketing-content-strategy` | `deliverables/marketing/03-content/content-strategy.md` | `content-strategy.xlsx` |
| `marketing-copywriting` | `deliverables/marketing/03-content/copywriting/` | `copy-library.xlsx` |
| `marketing-visual-content` | `deliverables/marketing/03-content/visual-content/` | `visual-style-guide.xlsx` |
| `marketing-social-content` | `deliverables/marketing/04-acquisition/social-content/` | `social-calendar.xlsx` |
| `marketing-paid-advertising` | `deliverables/marketing/04-acquisition/paid-advertising.md` | `paid-advertising-blueprint.xlsx` |
| `marketing-email-outreach` | `deliverables/marketing/04-acquisition/email-outreach/` | `prospect-research.xlsx`、`sequence-builder.xlsx` |
| `marketing-landing-page` | `deliverables/marketing/05-cro/landing-page.md` | `cro-experiment-queue.xlsx` |
| `marketing-funnel-optimization` | `deliverables/marketing/05-cro/funnel-optimization.md` | `funnel-redesign.xlsx` |
| `marketing-inquiry-flow` | `deliverables/marketing/05-cro/inquiry-flow.md` | `inquiry-flow-optimization.xlsx` |
| `marketing-launch-strategy` | `deliverables/marketing/06-growth/launch-strategy.md` | `launch-strategy.xlsx` |
| `marketing-referral-program` | `deliverables/marketing/06-growth/referral-program.md` | `referral-program-design.xlsx` |
| `marketing-retention` | `deliverables/marketing/06-growth/retention.md` | `retention-strategy.xlsx` |
| `marketing-analytics-and-optimization` | `deliverables/marketing/07-measurement/analytics-and-optimization.md` | `analytics-and-optimization.xlsx` |

辅助 skill（非战役阶段）：`marketing-copy-editing`、`marketing-psychology`。评测报告：`deliverables/marketing/<阶段>/review/<skill>-review.md`。

## 依赖边

```
marketing-positioning -> []
marketing-competitor-intelligence -> []
marketing-pricing-strategy -> [marketing-positioning, marketing-competitor-intelligence]

marketing-seo-audit -> [marketing-positioning, marketing-competitor-intelligence]
marketing-ai-seo -> [marketing-seo-audit]
marketing-programmatic-seo -> [marketing-seo-audit, marketing-competitor-intelligence]
marketing-site-and-schema -> [marketing-seo-audit, marketing-programmatic-seo]

marketing-content-strategy -> [marketing-positioning, marketing-competitor-intelligence, marketing-seo-audit]
marketing-copywriting -> [marketing-content-strategy, marketing-positioning]
marketing-visual-content -> [marketing-content-strategy, marketing-copywriting]

marketing-social-content -> [marketing-content-strategy, marketing-positioning]
marketing-paid-advertising -> [marketing-positioning, marketing-competitor-intelligence, marketing-pricing-strategy]
marketing-email-outreach -> [marketing-positioning, marketing-competitor-intelligence]

marketing-landing-page -> [marketing-positioning, marketing-copywriting]
marketing-inquiry-flow -> [marketing-positioning]
marketing-funnel-optimization -> [marketing-landing-page, marketing-inquiry-flow]

marketing-launch-strategy -> [marketing-positioning, marketing-content-strategy, marketing-competitor-intelligence]
marketing-referral-program -> [marketing-positioning, marketing-pricing-strategy]
marketing-retention -> [marketing-inquiry-flow, marketing-email-outreach, marketing-pricing-strategy]

marketing-analytics-and-optimization -> [marketing-landing-page, marketing-paid-advertising, marketing-funnel-optimization]
```

无硬依赖的节点可并行；有硬依赖的必须串行。

## 状态判定

- `approved` 的意思是「已过证据闸」：AI 按 `docs/feedback-rules.md` 第 9 节逐条自查通过后，在 frontmatter 写 `status: approved` 和 `evidence_gate: <日期>`。不需要操作者批准；操作者只决定发不发、上不上。
- 文件产出：看 frontmatter `status: approved`。
- 目录产出：至少 1 个 `.md` 为 `approved`。
- 文件在但没过证据闸 → `draft`。
- 文件不在 → `missing`。
- 方法 `SKILL.md` 不在 → 该节点不可跑，编排器停并写缺口。

## 闸门

- 产品上下文：台账 `product_context` 可读，否则停。
- 硬依赖：上游为 `approved`（已过证据闸），或台账「豁免」表记录了 `user_waiver`。
- 证据闸：交付物交给操作者去做、去发、去上线前，过 `docs/feedback-rules.md` 第 9 节清单。
- 评审：交付物 `review.status: passed` 或显式 `user_waiver`。评审由 AI 跑评测 skill 做，不是操作者审批。
- 反馈闸：上线、发出以后，看底表里的 L1–L3（经 `scripts/next_step.py` 读），不看操作者的意见。
- 产出：策略文档与表进 `deliverables/marketing/<阶段>/`；评审进 `deliverables/marketing/<阶段>/review/`；元产出进 `deliverables/marketing/00-system/`；进度只写 `state/marketing-status.md`。

## 附属贡献

专项子工作写入上表正典交付物，不另开一套文件名。

| 工作 | 归入 |
| --- | --- |
| 广告创意、视频脚本、提示词 | `marketing-visual-content` 的 `visual-style-guide.xlsx` |
| 转化研究摘录 | `marketing-landing-page` 的 `cro-experiment-queue.xlsx` |
| 市场体量、关键词需求 | `deliverables/marketing/00-research/`，并回写 `positioning-data.xlsx` / `seo-audit-data.xlsx` |
| SEO 路线 | `marketing-seo-audit` 的 `seo-audit-data.xlsx` |

## 机器可读图

```json
{
  "version": 3,
  "global_gates": {
    "product_context": {
      "ledger_key": "product_context",
      "default": "docs/fact-sources.md",
      "block_if_unreadable": true
    },
    "evidence_gate": {
      "checklist": "docs/feedback-rules.md#9",
      "pass_frontmatter": {"status": "approved", "evidence_gate": "<date>"},
      "set_by": "ai"
    },
    "review": {
      "required": true,
      "pass_status": "passed",
      "waiver_field": "user_waiver"
    }
  },
  "output_policy": {
    "strategy_docs": "deliverables/marketing/<phase>/",
    "tables": "deliverables/marketing/<phase>/",
    "review_reports": "deliverables/marketing/<phase>/review/",
    "research": "deliverables/marketing/00-research/",
    "system": "deliverables/marketing/00-system/",
    "progress": "state/marketing-status.md"
  },
  "phases": [
    {
      "id": "0",
      "name": "product-context",
      "phase_dir": null,
      "skills": ["marketing-profile"]
    },
    {
      "id": "00-research",
      "name": "research",
      "phase_dir": "00-research",
      "skills": []
    },
    {
      "id": "00-system",
      "name": "system",
      "phase_dir": "00-system",
      "skills": [
        "marketing-teach",
        "marketing-eval",
        "marketing-evolve",
        "marketing-skill-eval"
      ]
    },
    {
      "id": "1",
      "name": "foundation",
      "entry_skill": "marketing-foundation",
      "phase_dir": "01-foundation",
      "skills": [
        "marketing-positioning",
        "marketing-competitor-intelligence",
        "marketing-pricing-strategy"
      ]
    },
    {
      "id": "2",
      "name": "seo",
      "entry_skill": "marketing-seo",
      "phase_dir": "02-seo",
      "skills": [
        "marketing-seo-audit",
        "marketing-ai-seo",
        "marketing-programmatic-seo",
        "marketing-site-and-schema"
      ]
    },
    {
      "id": "3",
      "name": "content",
      "entry_skill": "marketing-content",
      "phase_dir": "03-content",
      "skills": [
        "marketing-content-strategy",
        "marketing-copywriting",
        "marketing-visual-content"
      ]
    },
    {
      "id": "4",
      "name": "acquisition",
      "entry_skill": "marketing-acquisition",
      "phase_dir": "04-acquisition",
      "skills": [
        "marketing-social-content",
        "marketing-paid-advertising",
        "marketing-email-outreach"
      ]
    },
    {
      "id": "5",
      "name": "cro",
      "entry_skill": "marketing-cro",
      "phase_dir": "05-cro",
      "skills": [
        "marketing-landing-page",
        "marketing-inquiry-flow",
        "marketing-funnel-optimization"
      ]
    },
    {
      "id": "6",
      "name": "growth",
      "entry_skill": "marketing-growth",
      "phase_dir": "06-growth",
      "skills": [
        "marketing-launch-strategy",
        "marketing-referral-program",
        "marketing-retention"
      ]
    },
    {
      "id": "7",
      "name": "measurement",
      "entry_skill": "marketing-measurement",
      "phase_dir": "07-measurement",
      "skills": ["marketing-analytics-and-optimization"]
    }
  ],
  "registry": {
    "marketing-positioning": {
      "phase": "01-foundation",
      "output": "deliverables/marketing/01-foundation/product-positioning.md",
      "tables": ["deliverables/marketing/01-foundation/positioning-data.xlsx"],
      "review": "deliverables/marketing/01-foundation/review/positioning-review.md",
      "dependencies": []
    },
    "marketing-competitor-intelligence": {
      "phase": "01-foundation",
      "output": "deliverables/marketing/01-foundation/competitor-analysis.md",
      "tables": ["deliverables/marketing/01-foundation/competitor-profiles.xlsx"],
      "review": "deliverables/marketing/01-foundation/review/competitor-intelligence-review.md",
      "dependencies": []
    },
    "marketing-pricing-strategy": {
      "phase": "01-foundation",
      "output": "deliverables/marketing/01-foundation/pricing-strategy.md",
      "tables": ["deliverables/marketing/01-foundation/pricing-benchmark.xlsx"],
      "review": "deliverables/marketing/01-foundation/review/pricing-strategy-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"}
      ]
    },
    "marketing-seo-audit": {
      "phase": "02-seo",
      "output": "deliverables/marketing/02-seo/seo-audit.md",
      "tables": ["deliverables/marketing/02-seo/seo-audit-data.xlsx"],
      "review": "deliverables/marketing/02-seo/review/seo-audit-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"}
      ]
    },
    "marketing-ai-seo": {
      "phase": "02-seo",
      "output": "deliverables/marketing/02-seo/ai-seo.md",
      "tables": ["deliverables/marketing/02-seo/ai-visibility-report.xlsx"],
      "review": "deliverables/marketing/02-seo/review/ai-seo-review.md",
      "dependencies": [
        {"skill": "marketing-seo-audit", "type": "hard"}
      ]
    },
    "marketing-programmatic-seo": {
      "phase": "02-seo",
      "output": "deliverables/marketing/02-seo/programmatic-seo.md",
      "tables": ["deliverables/marketing/02-seo/pseo-page-matrix.xlsx"],
      "review": "deliverables/marketing/02-seo/review/programmatic-seo-review.md",
      "dependencies": [
        {"skill": "marketing-seo-audit", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"}
      ]
    },
    "marketing-site-and-schema": {
      "phase": "02-seo",
      "output": "deliverables/marketing/02-seo/site-and-schema.md",
      "tables": ["deliverables/marketing/02-seo/site-schema-blueprint.xlsx"],
      "review": "deliverables/marketing/02-seo/review/site-and-schema-review.md",
      "dependencies": [
        {"skill": "marketing-seo-audit", "type": "hard"},
        {"skill": "marketing-programmatic-seo", "type": "hard"}
      ]
    },
    "marketing-content-strategy": {
      "phase": "03-content",
      "output": "deliverables/marketing/03-content/content-strategy.md",
      "tables": ["deliverables/marketing/03-content/content-strategy.xlsx"],
      "review": "deliverables/marketing/03-content/review/content-strategy-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"},
        {"skill": "marketing-seo-audit", "type": "hard"}
      ]
    },
    "marketing-copywriting": {
      "phase": "03-content",
      "output": "deliverables/marketing/03-content/copywriting/index.md",
      "tables": ["deliverables/marketing/03-content/copywriting/copy-library.xlsx"],
      "review": "deliverables/marketing/03-content/review/copywriting-review.md",
      "dependencies": [
        {"skill": "marketing-content-strategy", "type": "hard"},
        {"skill": "marketing-positioning", "type": "hard"}
      ]
    },
    "marketing-visual-content": {
      "phase": "03-content",
      "output": "deliverables/marketing/03-content/visual-content/index.md",
      "tables": ["deliverables/marketing/03-content/visual-style-guide.xlsx"],
      "review": "deliverables/marketing/03-content/review/visual-content-review.md",
      "dependencies": [
        {"skill": "marketing-content-strategy", "type": "hard"},
        {"skill": "marketing-copywriting", "type": "hard"}
      ]
    },
    "marketing-social-content": {
      "phase": "04-acquisition",
      "output": "deliverables/marketing/04-acquisition/social-content/index.md",
      "tables": ["deliverables/marketing/04-acquisition/social-calendar.xlsx"],
      "review": "deliverables/marketing/04-acquisition/review/social-content-review.md",
      "dependencies": [
        {"skill": "marketing-content-strategy", "type": "hard"},
        {"skill": "marketing-positioning", "type": "hard"}
      ]
    },
    "marketing-paid-advertising": {
      "phase": "04-acquisition",
      "output": "deliverables/marketing/04-acquisition/paid-advertising.md",
      "tables": ["deliverables/marketing/04-acquisition/paid-advertising-blueprint.xlsx"],
      "review": "deliverables/marketing/04-acquisition/review/paid-advertising-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"},
        {"skill": "marketing-pricing-strategy", "type": "hard"}
      ]
    },
    "marketing-email-outreach": {
      "phase": "04-acquisition",
      "output": "deliverables/marketing/04-acquisition/email-outreach/index.md",
      "tables": [
        "deliverables/marketing/04-acquisition/email-outreach/prospect-research.xlsx",
        "deliverables/marketing/04-acquisition/email-outreach/sequence-builder.xlsx"
      ],
      "review": "deliverables/marketing/04-acquisition/review/email-outreach-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"}
      ]
    },
    "marketing-landing-page": {
      "phase": "05-cro",
      "output": "deliverables/marketing/05-cro/landing-page.md",
      "tables": ["deliverables/marketing/05-cro/cro-experiment-queue.xlsx"],
      "review": "deliverables/marketing/05-cro/review/landing-page-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-copywriting", "type": "hard"}
      ]
    },
    "marketing-funnel-optimization": {
      "phase": "05-cro",
      "output": "deliverables/marketing/05-cro/funnel-optimization.md",
      "tables": ["deliverables/marketing/05-cro/funnel-redesign.xlsx"],
      "review": "deliverables/marketing/05-cro/review/funnel-optimization-review.md",
      "dependencies": [
        {"skill": "marketing-landing-page", "type": "hard"},
        {"skill": "marketing-inquiry-flow", "type": "hard"}
      ]
    },
    "marketing-inquiry-flow": {
      "phase": "05-cro",
      "output": "deliverables/marketing/05-cro/inquiry-flow.md",
      "tables": ["deliverables/marketing/05-cro/inquiry-flow-optimization.xlsx"],
      "review": "deliverables/marketing/05-cro/review/inquiry-flow-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"}
      ]
    },
    "marketing-launch-strategy": {
      "phase": "06-growth",
      "output": "deliverables/marketing/06-growth/launch-strategy.md",
      "tables": ["deliverables/marketing/06-growth/launch-strategy.xlsx"],
      "review": "deliverables/marketing/06-growth/review/launch-strategy-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-content-strategy", "type": "hard"},
        {"skill": "marketing-competitor-intelligence", "type": "hard"}
      ]
    },
    "marketing-referral-program": {
      "phase": "06-growth",
      "output": "deliverables/marketing/06-growth/referral-program.md",
      "tables": ["deliverables/marketing/06-growth/referral-program-design.xlsx"],
      "review": "deliverables/marketing/06-growth/review/referral-program-review.md",
      "dependencies": [
        {"skill": "marketing-positioning", "type": "hard"},
        {"skill": "marketing-pricing-strategy", "type": "hard"}
      ]
    },
    "marketing-retention": {
      "phase": "06-growth",
      "output": "deliverables/marketing/06-growth/retention.md",
      "tables": ["deliverables/marketing/06-growth/retention-strategy.xlsx"],
      "review": "deliverables/marketing/06-growth/review/retention-review.md",
      "dependencies": [
        {"skill": "marketing-inquiry-flow", "type": "hard"},
        {"skill": "marketing-email-outreach", "type": "hard"},
        {"skill": "marketing-pricing-strategy", "type": "hard"}
      ]
    },
    "marketing-analytics-and-optimization": {
      "phase": "07-measurement",
      "output": "deliverables/marketing/07-measurement/analytics-and-optimization.md",
      "tables": ["deliverables/marketing/07-measurement/analytics-and-optimization.xlsx"],
      "review": "deliverables/marketing/07-measurement/review/analytics-and-optimization-review.md",
      "dependencies": [
        {"skill": "marketing-landing-page", "type": "hard"},
        {"skill": "marketing-paid-advertising", "type": "hard"},
        {"skill": "marketing-funnel-optimization", "type": "hard"}
      ]
    }
  }
}
```
