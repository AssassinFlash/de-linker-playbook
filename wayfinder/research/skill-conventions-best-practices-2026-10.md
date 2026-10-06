---
wayfinder: research
created: 2026-10-06
status: complete
feeds: extraction-spec
---

# Skill conventions and authoring best practices (2026-10)

Decision-oriented brief for extracting ~80 marketing/lead-gen skills into a **cross-harness playbook**. Claims below are traced to first-party docs unless marked *secondary*. Retrieved 2026-10-06.

**Two facts this ticket answers**

1. What the Agent Skills / `SKILL.md` spec actually requires, and how official authoring guides say to write it.
2. What each major harness auto-discovers for skills vs standing instructions, and which paths are shared vs adapter-only.

---

## 0. Decisions this should lock for the extraction spec

| Decision | Recommendation | Why |
| --- | --- | --- |
| Canonical skill format | Directory `skill-name/SKILL.md` with YAML `name` + `description` only; Markdown body; optional `references/`, `scripts/`, `assets/` | Open spec required fields are just those two. Extra frontmatter is vendor-specific and breaks portability. |
| Canonical skill location | **Content:** `skills/<name>/SKILL.md` (flat, one folder per skill). **Discovery:** generate thin adapters into `.agents/skills/` (required) and `.claude/skills/` (Claude Code). | `.agents/skills/` is the de-facto shared scan path. Claude Code still only documents `.claude/skills/`. Root `skills/` is human-readable and matches this repo’s map; no harness auto-scans a bare `skills/` folder. |
| Standing instructions | One root `AGENTS.md` (short). Do **not** also ship a `CLAUDE.md` unless Claude-only overrides are needed. | `AGENTS.md` is the multi-vendor always-on file. Claude Code now reads it on its own or alongside `CLAUDE.md`. Dual files drift. |
| Body budget | `SKILL.md` body **< 500 lines and < 5,000 tokens**. Move the rest behind one-level-deep relative links. | Spec + Anthropic authoring guide. ~80 skills × fat bodies will blow catalogs (Codex 2% / 8k-char list; Zed 50 KB catalog). |
| Description budget | Target **300–700 characters**, hard cap 1024. Must include **what** + **when** (trigger phrases). No XML. | Spec max 1024. Codex shortens descriptions under catalog pressure; front-load triggers. |
| Harness-only fields | **Forbidden in canonical skills:** `allowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `disable-model-invocation`, `user-invocable`, `whenToUse`, `arguments`, `type`, MCP tool IDs, `$ARGUMENTS` / `${KIMI_SKILL_DIR}` | Those are Claude / Cursor / Kimi / VS Code extensions. Put them only in generated adapters if a harness ever needs them. |
| Tools in body | Capability language (“use web search”, “run a shell command”), never `mcp__*` names | Map constraint + portability. |
| Examples | Teaching scaffolds only; label every example **「仅供理解，禁止引用到输出」** (or EN equivalent) and keep bulky examples in `references/examples.md` | Map constraint + official “one-level-deep references” pattern. |

If extraction has to pick **one** auto-discovered folder and skip adapters: put skills in `.agents/skills/` (widest native scan). Claude Code then needs a symlink or it will not see them.

---

## 1. Official SKILL.md spec (latest)

**Primary sources**

- Spec: <https://agentskills.io/specification>
- Overview: <https://agentskills.io/home>
- Authoring: <https://agentskills.io/skill-creation/best-practices>
- Description evals: <https://agentskills.io/skill-creation/optimizing-descriptions>
- Client implementors (where to scan): <https://agentskills.io/client-implementation/adding-skills-support>
- Anthropic engineering: <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
- Anthropic platform overview: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
- Anthropic authoring: <https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices> (canonical URL redirects to platform.claude.com)
- Reference implementation: <https://github.com/anthropics/skills>
- Validator: `skills-ref validate` at <https://github.com/agentskills/agentskills/tree/main/skills-ref>

The format was created by Anthropic, released as an open standard at agentskills.io, and is now implemented by many clients (Claude Code, Codex, Cursor, Gemini CLI, Copilot, Zed, Goose, Amp, OpenCode, … — listed on the spec home). The spec defines **what is inside a skill folder**. It does **not** mandate where that folder lives on disk.

### 1.1 Directory shape

```
skill-name/
├── SKILL.md          # required: YAML frontmatter + Markdown instructions
├── scripts/          # optional: executable code
├── references/       # optional: on-demand docs
├── assets/           # optional: templates, images, data
└── …                 # any other files
```

A skill is discovered as a **subdirectory containing a file named exactly `SKILL.md`**. Filename capitalization matters on case-sensitive filesystems.

### 1.2 Frontmatter — allowed fields

| Field | Required | Constraints (spec) | Portable? |
| --- | --- | --- | --- |
| `name` | **Yes** | 1–64 chars. Unicode lowercase alphanumeric + hyphens. Must not start/end with `-`. Must not contain `--`. **Must match parent directory name.** | Yes — required everywhere. |
| `description` | **Yes** | 1–1024 chars, non-empty. What it does **and when to use it**. Include keywords agents can match. | Yes — this is the trigger. |
| `license` | No | Short license name or bundled license filename. | Optional; fine if this repo needs one. |
| `compatibility` | No | 1–500 chars. Env requirements (product, packages, network). “Most skills do not need this.” | Skip unless a skill truly needs git/docker/Python X. |
| `metadata` | No | Map of string → string. Clients store extra properties. “Make key names reasonably unique.” | Optional `author` / `version` only. Do not stuff harness flags here. |
| `allowed-tools` | No | **Experimental.** Space-separated pre-approved tools. Support varies. | **Do not put in canonical skills.** Claude-shaped (`Bash(git:*) Read`). |

**Anthropic extra constraints** (platform overview; slightly stricter than the open spec):

- `name`: no XML tags; reserved words **`anthropic`** and **`claude`** forbidden.
- `description`: no XML tags (`<` `>`). Frontmatter is injected into the system prompt; angle brackets are an injection hazard.

**Minimal legal file**

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

**Good optional example (spec)**

```yaml
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```

Invalid `name` examples from the spec: `PDF-Processing` (uppercase), `-pdf` (leading hyphen), `pdf--processing` (consecutive hyphens).

### 1.3 How `description` must be written (this is the trigger)

The description is **tier-1 catalog text**. At startup every client loads only `name` + `description` (~50–100 tokens/skill). The model never sees the body until it decides the skill matches.

Official rules, collapsed:

1. **Both jobs in one field:** what the skill does **and** when to use it. ([spec](https://agentskills.io/specification#description-field), [Anthropic overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Anthropic authoring](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices))
2. **Specific keywords / user-intent phrases**, including cases where the user does not name the domain. ([optimizing-descriptions](https://agentskills.io/skill-creation/optimizing-descriptions): “even if they don’t explicitly mention ‘CSV’”)
3. **Imperative is preferred by the open authoring guide:** “Use this skill when…” rather than “This skill does…”.
4. **Front-load the use case.** Codex shortens descriptions when the catalog exceeds **2% of context or 8,000 characters**; later sentences may be dropped. ([Codex skills](https://developers.openai.com/codex/skills))
5. **One description per skill.** It is the only signal for selection among 100+ skills. Implementation belongs in the body.

**Official good / bad (spec + Anthropic)**

```
# Good
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.

# Bad
description: Helps with PDFs.
description: Processes data.
description: Does stuff with files.
```

**Optimizing-descriptions “after” pattern (keep under 1024):**

```
description: >
  Analyze CSV and tabular data files — compute summary statistics,
  add derived columns, generate charts, and clean messy data. Use this
  skill when the user has a CSV, TSV, or Excel file and wants to
  explore, transform, or visualize the data, even if they don't
  explicitly mention "CSV" or "analysis."
```

Nuance from the same guide: agents often **skip** a skill for a one-step task they can already do (“read this PDF”). Descriptions matter most for specialized workflows, not trivial tool use.

Lenient parsers: unquoted `description: Use this skill when: the user asks…` is invalid YAML (colon). Prefer `>` block scalars. ([client implementation](https://agentskills.io/client-implementation/adding-skills-support))

### 1.4 Progressive disclosure (the load model)

| Tier | What | When | Cost |
| --- | --- | --- | --- |
| 1 Metadata | `name` + `description` | Session start, all skills | ~50–100 tokens each |
| 2 Instructions | Full `SKILL.md` body | Skill activated | **< 5,000 tokens recommended** |
| 3 Resources | `scripts/`, `references/`, `assets/` | Only when the body tells the agent to load/run them | 0 until accessed. Scripts: only **stdout** enters context |

This is the same model in the spec, Anthropic’s engineering post, Claude platform docs, Codex, Cursor, Gemini CLI, Copilot, and Zed.

**Body length:** keep `SKILL.md` **under 500 lines** (spec + Anthropic). Split before you hit it. SKILL.md is a **table of contents + the procedure needed on every run**, not the encyclopedia.

**File references**

- Relative to the skill root: `references/REFERENCE.md`, `scripts/extract.py`.
- **One level deep from SKILL.md.** Nested chains (`SKILL.md` → `advanced.md` → `details.md`) cause partial reads (`head -100`) and missed content. ([Anthropic authoring](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices), spec)
- Tell the agent **when** to open each file: “Read `references/api-errors.md` if the API returns a non-200” beats “see references/”.
- Forward slashes only (`scripts/helper.py`, never `scripts\helper.py`).
- Reference files **> 100 lines** should start with a table of contents (Anthropic: agents preview with partial reads).

**What belongs where**

| Put in | Content |
| --- | --- |
| Frontmatter `description` | Trigger only |
| `SKILL.md` body | Core procedure, defaults, gotchas that fire before the agent knows to look them up, checklist, pointers |
| `references/` | Domain dumps, schemas, long API notes, bulky example banks |
| `scripts/` | Deterministic work the agent would otherwise reinvent; run, don’t paste |
| `assets/` | Output templates, fonts, sample files the agent copies into a deliverable |

### 1.5 Official body-writing rules (anti-patterns included)

From [agentskills.io best practices](https://agentskills.io/skill-creation/best-practices) and [Anthropic authoring](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices). These are the extraction-spec acceptance bar.

**Do**

- Start from real expertise (runbooks, corrections, actual I/O), not “generate a skill from general knowledge”.
- Add only what the model **would get wrong without the skill**. Cut “what is a PDF”.
- One coherent unit of work (function-sized). Too narrow → many skills load and conflict. Too broad → can’t trigger precisely.
- Moderate detail. Exhaustive edge-case novels make the agent follow irrelevant branches.
- Match control to fragility: high freedom for judgment tasks; exact commands for migrations / deploys.
- **Defaults, not menus.** One recommended tool + one escape hatch.
- **Procedures, not instance answers.** Teach how to approach a class of problems.
- Gotchas in SKILL.md (not a buried reference) when they defy reasonable assumptions.
- Output templates (inline if short; `assets/` if long or conditional).
- Checklists for multi-step work; validate-then-fix loops; plan-validate-execute for batch/destructive work.
- Consistent terminology. No time-bombs (“before August 2025 use the old API”) — put legacy under an “old patterns” details block.
- Concrete input/output examples when quality depends on seeing the shape.
- Scripts that **handle errors**; no magic constants; list install steps instead of assuming packages exist.
- Unix paths; fully-qualified MCP names **only in a Claude-only adapter**, never in canonical copy.

**Don’t (named anti-patterns)**

| Anti-pattern | Source |
| --- | --- |
| Vague description (`Helps with documents`) | Anthropic authoring, spec |
| Explaining knowledge the model already has | Both authoring guides |
| Offering four libraries as equals | Anthropic “Avoid offering too many options”; skills.io “Provide defaults, not menus” |
| Deeply nested reference chains | Anthropic + spec |
| Windows backslash paths | Anthropic |
| Time-sensitive instructions in the main path | Anthropic |
| Inconsistent terms for the same thing | Anthropic |
| LLM-generated generic procedures with no project context | skills.io “Start from real expertise” |
| Skill that restates a one-off SQL query instead of a method | skills.io “Favor procedures over declarations” |
| `name` containing `claude` / `anthropic` | Anthropic; also illustrated by anthropics/skills renaming `claude-academy-guide` → `academy-guide` |
| Description > 1024 chars (upload validation rejects) | anthropics/skills README commit notes |
| XML / angle brackets in frontmatter | Anthropic overview |
| Assuming packages/tools are installed | Anthropic |
| Scripts that just throw and “let Claude figure it out” | Anthropic |
| Putting everything in CLAUDE.md / AGENTS.md instead of skills | Anthropic engineering: context window is a public good |

Anthropic checklist before shipping: specific description with what+when; body < 500 lines; extra detail in separate files; no time-bombs; consistent terms; concrete examples; one-level-deep refs; workflows with steps; (if code) error handling, listed packages, forward slashes, validation loops.

### 1.6 Vendor frontmatter that is **not** in the open spec

Do not copy these into extracted canonical skills. They are why “thin adapters” exist.

| Field | Who | Effect |
| --- | --- | --- |
| `allowed-tools` / `disallowed-tools` | Spec experimental; Claude Code | Pre-approve tools |
| `disable-model-invocation` | Claude, Cursor, VS Code, Zed, Kimi (also `disableModelInvocation`) | Hide from auto catalog; slash-only |
| `user-invocable` | Claude, VS Code | Hide from `/` menu |
| `when_to_use` / `whenToUse` | Claude directory listing; Kimi | Extra trigger text (Kimi also uses `description`) |
| `argument-hint` / `arguments` | Claude, VS Code, Kimi | Slash-command args (`$0`, `$pr_ref`) |
| `paths` / legacy `globs` | Cursor, Claude | File-glob scoping |
| `model`, `effort`, `context`, `agent`, `background`, `hooks`, `shell` | Claude Code | Execution / subagent / injection |
| `icon`, `color` | Cursor Custom Modes | UI badge |
| `context: fork` | VS Code / Copilot (experimental), Claude | Run skill in a subagent |
| `type: prompt \| flow` | Kimi | Flow skills are manual-only |
| `agents/openai.yaml` | Codex / ChatGPT | UI metadata, `allow_implicit_invocation`, MCP deps |

---

## 2. Recommended canonical SKILL.md (maximum portability)

Use this as the extraction template. Folder name **equals** `name`.

```markdown
---
name: marketing-example-skill
description: >
  Write X for Y audience. Use when the user asks to draft, rewrite, or
  review X, or mentions Y / Z trigger phrases — even if they do not
  say the skill name.
---

# Marketing example skill

One or two sentences of purpose. No product lock-in. No harness tool IDs.

## When this applies

- Bullet the branches the description already named (keep this short; the
  description is the real trigger).
- Point to sibling skills when the task is adjacent, not this one.

## Procedure

1. Step with a checkable done-condition.
2. Default tool/approach. One escape hatch, not a menu.
3. If condition C, read [references/edge-cases.md](references/edge-cases.md).
4. Validate output against the checklist below before returning.

## Defaults

- Prefer A. Use B only when A cannot work because …

## Gotchas

- Concrete, environment-specific facts the model will get wrong otherwise.

## Output

Use this shape (adapt sections, do not invent a parallel format):

```markdown
# [title]
...
```

## Examples

> 仅供理解，禁止引用到输出。 Teaching scaffolds only — never copy wording into a deliverable.

Keep 1–2 tiny examples inline. Move the rest to
[references/examples.md](references/examples.md) and tell the agent when to open it.

## Checklist

- [ ] …
```

**Acceptance gates for every extracted skill**

- [ ] `name` matches folder; `^[a-z0-9]+(-[a-z0-9]+)*$`; ≤ 64 chars; no `claude`/`anthropic`
- [ ] `description` 1–1024 chars, what + when, no `<` `>`
- [ ] No vendor-only frontmatter keys
- [ ] Body < 500 lines / < 5k tokens
- [ ] Relative, one-level-deep, forward-slash paths
- [ ] Tools described as capabilities
- [ ] Examples labeled as non-citable
- [ ] No absolute machine paths; Linker facts pointed at `~/Documents/New`, not copied

---

## 3. Cross-harness discovery (2026-10)

Two layers, do not conflate them:

1. **Standing instructions** (always loaded): `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / rules files.
2. **Skills** (progressive): folders with `SKILL.md`, cataloged by name+description.

### 3.1 AGENTS.md — verified multi-vendor standing instructions

**Primary:** <https://agents.md/>

- Plain Markdown, **no required fields**. “A README for agents.”
- Emerged from Codex, Amp, Google Jules, Cursor, Factory. Now **stewarded by the Agentic AI Foundation under the Linux Foundation**. Site claims 60k+ open-source projects.
- Suggested sections: overview, build/test commands, code style, testing, security.
- Nested `AGENTS.md` in monorepos is an intended pattern.
- FAQ on that site: configure **Aider** with `.aider.conf.yml` → `read: AGENTS.md`; configure **Gemini CLI** with `.gemini/settings.json` → `"context": { "fileName": "AGENTS.md" }`.

**Who reads it natively (first-party)**

| Harness | AGENTS.md | Notes |
| --- | --- | --- |
| OpenAI Codex | **Primary.** Walks git root → CWD. Also `~/.codex/AGENTS.md`. Per-dir `AGENTS.override.md` wins over `AGENTS.md`. Default cap **32 KiB** (`project_doc_max_bytes`). | <https://developers.openai.com/codex/agent-configuration/agents-md> |
| Cursor | Yes (root + nested). Also `CLAUDE.md` at root as rules. Plus `.cursor/rules/*.mdc`. | Cursor skills/rules docs |
| GitHub Copilot / VS Code | Yes, as one instruction format among `.github/copilot-instructions.md`, `CLAUDE.md`, `GEMINI.md`. | VS Code custom-instructions + Copilot docs |
| Zed Agent | **Primary** project file (also accepts `.rules`, `.cursorrules`, `CLAUDE.md`, `GEMINI.md`, … first-match list). Personal: `~/.config/zed/AGENTS.md`. | <https://zed.dev/docs/ai/instructions> |
| Kimi Code | Project `AGENTS.md` (any subdirectory); user `~/.kimi/AGENTS.md` (help center). Injected as `${agents_md}`. | <https://www.kimi.com/en/help/kimi-code/cli-customization>, <https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html> |
| Claude Code | **Yes.** Official memory page: Claude “can also read a repository’s AGENTS.md files, **on their own or alongside CLAUDE.md**.” | <https://code.claude.com/docs/en/memory> |
| Gemini CLI | Default file is **`GEMINI.md`**. Reads `AGENTS.md` if `context.fileName` includes it. | agents.md FAQ; Gemini config |
| Aider | **Not auto.** Must `read: AGENTS.md` in `.aider.conf.yml` or `/read-only`. | agents.md FAQ |
| Continue | Native always-on is **`.continue/rules`**, not AGENTS.md. | <https://docs.continue.dev/customize/rules> |

**Implication:** a root `AGENTS.md` is the right always-on file for this repo. Keep it a **map** (how to work here, where skills live, pointer to Linker facts). Do not paste 80 skill bodies into it.

Do **not** create `CLAUDE.md` as a second copy. Claude Code will read `AGENTS.md`. If both exist, you get duplication and drift. Only add `CLAUDE.md` later for Claude-only permissions/MCP — not for playbook rules.

### 3.2 Skills — per-harness scan paths

**Shared convention (not in the SKILL.md spec, but in the official client-implementation guide):** scan both `.<client>/skills/` and **`.agents/skills/`** at project and user scope. “The `.agents/skills/` paths have emerged as a widely-adopted convention for cross-client skill sharing.” Project skills override user skills on name collision. ([adding-skills-support](https://agentskills.io/client-implementation/adding-skills-support))

#### Per-harness table (project-level unless noted)

| Harness | Skills auto-scan (project) | Skills auto-scan (user) | Also scans | Standing instructions | Adapter needed for *this* playbook? |
| --- | --- | --- | --- | --- | --- |
| **OpenAI Codex CLI** | `.agents/skills` from **CWD up to repo root** (every ancestor) | `~/.agents/skills`; admin `/etc/codex/skills`; bundled SYSTEM | Symlinked skill folders followed. Optional `agents/openai.yaml` (Codex-only). Does **not** document `.claude/skills`. | `AGENTS.md` chain, 32 KiB | **None** if skills are in `.agents/skills/`. If canonical is `skills/`, symlink into `.agents/skills/`. |
| **Cursor** | `.agents/skills/`, `.cursor/skills/` (recursive; nested category folders OK; nested package `.cursor/skills` scoped to that tree) | `~/.agents/skills/`, `~/.cursor/skills/` | **Compatibility:** `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/` | `AGENTS.md`, `CLAUDE.md`, `.cursor/rules` | **None** if `.agents/skills/` exists. Extra Cursor fields (`paths`, `icon`) stay out of canonical. |
| **Gemini CLI** | `.gemini/skills/` **or alias `.agents/skills/`**. One level deep only (`skills/<name>/SKILL.md`). Workspace must be **trusted**. | `~/.gemini/skills/` or `~/.agents/skills/` | Extensions; built-ins. Precedence workspace > user > extension > built-in | Default `GEMINI.md`; `AGENTS.md` via `context.fileName` | **None** if `.agents/skills/`. Optionally set `context.fileName` to `AGENTS.md`. Note: unpaid Gemini CLI → **Antigravity CLI** as of 2026-06-18 (banner on geminicli.com). |
| **Kimi Code CLI** | `.kimi-code/skills/`, `.agents/skills/` (project root = nearest `.git`) | `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` | `extra_skill_dirs` in `config.toml`; built-ins lowest. Precedence **Project > User > Extra > Built-in** | `AGENTS.md` | **None** if `.agents/skills/`. Do not use Kimi-only keys (`type`, `whenToUse`, `arguments`) in canonical. Official CLI docs do **not** list `.claude/skills/` (ignore third-party claims). |
| **Zed Agent** | **Only** `<worktree>/.agents/skills/`. **Flat** — no `group/skill/` nesting. Trusted worktrees only. | `~/.agents/skills/` | No `.claude/`, no `.cursor/`, no custom paths (symlink if needed). 50 KB catalog cap. | `AGENTS.md` (and several fallbacks) | **None** if `.agents/skills/<name>/SKILL.md` is flat. Nested category folders would be **invisible**. |
| **GitHub Copilot / VS Code** | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | Plugin `chatSkills`. `name` must match folder or skill silently fails. | `AGENTS.md` / copilot-instructions / CLAUDE.md / GEMINI.md | **None** if `.agents/skills/` or `.claude/skills/`. `.github/skills/` is Copilot-idiomatic but redundant. |
| **Claude Code** | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/` | Plugins; `--add-dir`; nested `.claude/skills` with disambiguated `/apps/web:deploy`. Commands merged into skills (`.claude/commands/*.md` still work). | `CLAUDE.md` and/or `AGENTS.md`; `.claude/rules/` | **Yes.** Official docs do **not** list `.agents/skills/`. Adapter: symlink `.claude/skills/<name>` → canonical. |
| **Aider** | **None.** No skills scanner. | — | Load files with `/read-only` or `read:` in `.aider.conf.yml` | Only if configured to read `AGENTS.md` | **Yes.** Ship `.aider.conf.yml` with `read: AGENTS.md`. AGENTS.md must tell the agent to open `skills/<name>/SKILL.md` when relevant (poor man’s progressive disclosure). |
| **Continue** | **None** for SKILL.md. Uses `.continue/rules` (+ prompts). | — | Community “npx skills add” is a separate Continue-skills pack, not the open Agent Skills scanner | `.continue/rules` | **Yes, later.** Either generate `.continue/rules` pointers or rely on AGENTS.md. Do not block extraction on this. |
| **DeepSeek CLI / harness** | **No first-party Agent Skills product.** DeepSeek-the-model runs inside other harnesses (Codex-compatible, Kimi, Cursor, …) and inherits *that* harness’s paths. | — | Community “deepseek-cli” git repos that copy Gemini CLI docs are not DeepSeek official. | Whatever the wrapping harness reads | **No DeepSeek-specific adapter.** If a session uses DeepSeek *through Kimi/Codex/Cursor*, `.agents/skills/` already works. |
| **OpenAI Codex (ChatGPT desktop)** | Same `.agents/skills` model as CLI | `~/.agents/skills` | Plugins for distribution | `AGENTS.md` | Same as Codex CLI. |

### 3.3 What is de-facto standard vs adapter

**Standards (write once)**

| Artifact | Status |
| --- | --- |
| `SKILL.md` with `name` + `description` + Markdown body | Open spec. Universal. |
| `scripts/` `references/` `assets/` | Spec convention, widely honored. |
| **`.agents/skills/<name>/SKILL.md`** | De-facto **portable skill root**. Codex, Cursor, Gemini, Kimi, Zed, Copilot/VS Code. Recommended scan target in the official client guide. |
| **`AGENTS.md` at repo root** | De-facto **portable standing instructions**. AAIF/Linux Foundation. Codex, Cursor, Copilot, Zed, Kimi, Claude Code, Aider (config), Gemini (config). |
| Progressive disclosure (catalog → body → files) | Universal load model. |

**Not shared — generate only when a human actually uses that harness**

| Adapter | Why |
| --- | --- |
| `.claude/skills/` → canonical | Claude Code native path. Highest-priority adapter. |
| `.aider.conf.yml` `read: AGENTS.md` | Aider has no scanner. |
| `.gemini/settings.json` `context.fileName: AGENTS.md` | Gemini default is GEMINI.md. Skills still work via `.agents/skills` without this; this only unifies *instructions*. |
| `.github/skills/` | Only if Copilot users want the GitHub-native path; `.agents/skills` already counted. |
| `.cursor/skills/`, `.gemini/skills/`, `.kimi-code/skills/` | Redundant if `.agents/skills/` exists. Do not duplicate. |
| `CLAUDE.md`, `GEMINI.md`, `.continue/rules`, `.cursor/rules/*.mdc` | Vendor instruction files. Keep playbook rules in `AGENTS.md`. |
| `allowed-tools`, `$skill`, slash metadata | Harness wiring, not content. |

### 3.4 Catalog pressure at ~80 skills

80 × ~80 tokens ≈ 6.4k tokens of catalog if descriptions are tight; 80 × 1024 chars would blow Codex’s 8k-char list and Zed’s 50 KB cap. **Write short descriptions.** Prefer 300–700 characters. Codex will truncate; front-load triggers.

Zed and Gemini **do not discover nested** `skills/marketing/foo/`. Extraction **must** be flat: `skills/marketing-foo/`, not `skills/marketing/foo/`.

---

## 4. Where portable skills should live in this repo

### 4.1 Recommended layout

```
de-linker-playbook/
├── AGENTS.md                 # always-on map (short)
├── skills/                   # CANONICAL content (human + git)
│   ├── marketing-foo/
│   │   ├── SKILL.md
│   │   └── references/       # optional
│   └── lead-bar/
│       └── SKILL.md
├── .agents/skills/           # DISCOVERY ADAPTER (symlinks → ../../skills/…)
│   ├── marketing-foo → …
│   └── lead-bar → …
├── .claude/skills/           # CLAUDE ADAPTER (symlinks → ../../skills/…)
│   └── …                     # generate when Claude Code is actually used
├── schemas/ templates/ evals/ docs/ wayfinder/
└── .aider.conf.yml           # optional, Aider-only: read: AGENTS.md
```

**Why canonical = `skills/` rather than only `.agents/skills/`**

- This playbook’s map already committed to a flat `skills/` tree with `marketing-*` / `lead-*` names.
- Dot-directories are easy to miss in Git UIs; `skills/` is the product.
- Spec does not care about the parent path — only that each skill is a folder with `SKILL.md`.

**Why `.agents/skills/` adapter is not optional**

Without it, Codex, Zed, Gemini, Kimi, and Copilot **will not auto-activate** skills. They will only see whatever `AGENTS.md` narrates — which defeats progressive disclosure (80 full bodies must not be always-on).

**Why `.claude/skills/` is a thin adapter, not a second canonical tree**

Claude Code’s documented project path is `.claude/skills/<name>/SKILL.md` ([platform overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)). Cursor/Copilot already read `.claude/skills/` *and* `.agents/skills/`; Claude Code does not document the reverse.

Implementation: relative symlinks, not copies. One content tree.

### 4.2 What root `AGENTS.md` should contain (and not)

**Yes**

- One paragraph: this repo is a portable skill playbook; do not lock copy to a product SKU.
- Pointer: Linker product facts live in `~/Documents/New` (`CONTEXT.md`, `fact-base/`) — read, don’t copy.
- Pointer: skills are in `skills/<name>/SKILL.md`; if your harness auto-loads Agent Skills, they are also linked from `.agents/skills/` (and `.claude/skills/` for Claude Code).
- How to choose a skill: match the user task to a skill `description`; then follow that `SKILL.md`. Do not invent a parallel method.
- Build/test/eval commands once they exist.
- Example rule: skill examples are scaffolds; never quote them into deliverables.

**No**

- 80 skill bodies.
- Harness tool IDs.
- A second copy of CLAUDE.md content.

Keep well under Codex’s 32 KiB default. Aim for a few hundred lines, not thousands.

### 4.3 Extraction-spec implications (checklist to copy)

1. Output each skill as `skills/<kebab-name>/SKILL.md` with only `name` + `description`.
2. `name` = folder = `marketing-*` or `lead-*`, ≤ 64 characters.
3. After files exist, generate `.agents/skills/<name>` symlinks (part of repo-skeleton / extraction, not a later surprise).
4. Defer `.claude/skills/` until Claude Code is used — but document the one-liner so it is not redesigned.
5. Strip `allowed-tools`, `model`, `mcp__*`, `$ARGUMENTS`, `disable-model-invocation`, etc. on ingest.
6. Split any body > 500 lines into `references/` with explicit “read when…” lines.
7. Rewrite tool steps as capabilities.
8. Do not nest skill folders.
9. Do not ship `CLAUDE.md` as a clone of `AGENTS.md`.

---

## 5. Source list

### Spec and authoring

- https://agentskills.io/specification
- https://agentskills.io/home
- https://agentskills.io/skill-creation/best-practices
- https://agentskills.io/skill-creation/optimizing-descriptions
- https://agentskills.io/client-implementation/adding-skills-support
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- https://claude.com/blog/skills-explained
- https://github.com/anthropics/skills
- https://github.com/agentskills/agentskills

### Harness docs

- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code memory / AGENTS.md: https://code.claude.com/docs/en/memory
- Claude Code `.claude` directory: https://code.claude.com/docs/en/claude-directory
- Codex skills: https://developers.openai.com/codex/skills (renders as https://learn.chatgpt.com/docs/build-skills)
- Codex AGENTS.md: https://developers.openai.com/codex/agent-configuration/agents-md
- Cursor skills: https://cursor.com/docs/skills
- Gemini CLI skills: https://geminicli.com/docs/cli/tutorials/skills-getting-started , https://geminicli.com/docs/cli/using-agent-skills
- Kimi Code skills: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills
- Kimi Code AGENTS.md: https://www.kimi.com/en/help/kimi-code/cli-customization
- Zed skills: https://zed.dev/docs/ai/skills
- Zed instructions: https://zed.dev/docs/ai/instructions
- VS Code Agent Skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
- GitHub Copilot skills: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- AGENTS.md standard: https://agents.md/
- Continue rules: https://docs.continue.dev/customize/rules

### Not used as authority

Blog roundups that disagree on whether Claude Code reads AGENTS.md (several 2026 posts still say “no”). Official Claude Code memory page (retrieved 2026-10-06) says it does. Prefer that.

---

## 6. Gaps / follow-ups (do not block extraction)

- Claude Code’s **skills** scanner still not documented as reading `.agents/skills/`. Treat adapter as required until Anthropic says otherwise.
- Whether Antigravity CLI (Gemini successor on unpaid) keeps `.agents/skills/` — Gemini CLI docs still describe that path as of 2026-04-30 page update.
- Continue has no first-party SKILL.md loader; skip until someone uses Continue on this repo.
- DeepSeek has no official skills layout; inherit the wrapping harness.
- Do not run `skills-ref validate` here; extraction spec should add it as an acceptance command once skills exist.
