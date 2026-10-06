---
wayfinder: research
created: 2026-10-06
status: complete
feeds: [orchestration-workflow-form, pilot-slice, extraction-spec]
---

# Generic harness orchestration (2026-10)

Decision-oriented brief for driving **multi-step / phased agent workflows in harnesses that have no slash-command system**. Claims below are traced to first-party docs or the actual source repos unless marked *secondary*. Retrieved 2026-10-06.

This ticket answers four questions:

1. Does “one orchestrator skill reads a repo state file and tells the agent where it is / what next / where outputs go” actually work across harnesses?
2. Which harnesses have a subagent/Task equivalent, and can skill text trigger it?
3. Is there a portable prompt-file / command-file convention, or is everything vendor-specific?
4. What are the practical limits of `AGENTS.md` as a driver?

**The user’s skepticism is mostly right.** Claude-shaped orchestration that “just fires” is not a property of `SKILL.md`. In the wild it is a **bootstrap** (session-start hook / plugin / `GEMINI.md` import) plus a **catalog** (skill descriptions) plus **files on disk that survive compaction**. Without the bootstrap, a cold session only has `AGENTS.md` + whatever the harness auto-lists from `.agents/skills/`. That stack is real, and it is weaker than Claude slash commands. The rest of this note is evidence for how far it goes.

---

## 0. Decisions this should lock (for the orchestration-form ticket)

| Decision | Recommendation | Why |
| --- | --- | --- |
| Do not assume slash commands | Canonical playbook has **no** `.claude/commands/`, no `$ARGUMENTS`, no `/skill:name` as the driver. Commands are optional adapters. | Every major vendor is merging or deprecating command files into Agent Skills. Commands are not shared across harnesses. |
| Do not assume session-start hooks | Superpowers works because each harness **injects** `using-superpowers` at session start. This playbook will not ship 12 plugin manifests. Cold-start must work from `AGENTS.md` + skill catalog alone — **and that must be empirically tested**. | Superpowers’ own contributor rule: most new-harness PRs copied skill files and skipped bootstrap; they now require a clean-session transcript. |
| Orchestrator skill is a **navigator**, not a runtime | One short skill: read a state file → say current phase → name the next method skill → name the output path. Body uses capability language (“dispatch a subagent”, “read this file”), never `Task` / `Agent` / `mcp__*`. | Matches Superpowers’ portable-action style. Tool IDs are mapped per harness in Superpowers; we will not maintain that map. |
| Progress lives in **files**, not conversation | A small ledger / status markdown (checkboxes + “next”) is mandatory. Todos in the session are not enough. | Superpowers SDD: “Conversation memory does not survive compaction. Controllers that lost their place have re-dispatched entire completed task sequences.” |
| Subagents are optional acceleration | If the harness has a spawn tool, the orchestrator *may* ask for it. If not, the same session runs the next skill inline (Superpowers `executing-plans` fallback). | Six of seven target CLIs have a spawn equivalent. Aider does not. Skill frontmatter `context: fork` is Claude-only — do not put it in canonical skills. |
| `AGENTS.md` is a map, not a playbook | Root `AGENTS.md`: a few hundred lines max. Pointers to skills and to the state file. No phase procedures, no 80 skill bodies. | Codex silently truncates combined project docs at **32 KiB**. Anthropic: standing instructions are context, not enforcement; shorter → more followed. |
| User-invoked vs auto-invoked | Keep orchestrator **auto-invokable** (description starts with “Use when starting any … / when the user asks for marketing / SEO / content work”). Do **not** rely on `disable-model-invocation` — that is a Claude/Kimi extra and would hide the skill from auto-trigger, which is the only trigger we have without slash. | mattpocock marks routers `disable-model-invocation: true` because they expect `/ask-matt`. We do not. |

If the pilot proves that `AGENTS.md` + catalog **does not** auto-load the orchestrator on a given harness, the fallback is option 丙 (paste a command card) for that harness — not a rewrite of every skill.

---

## 1. Orchestrator-skill pattern — does it work?

### 1.1 What “works” actually means in 2026

Three layers, in increasing order of harness coupling:

| Layer | What it is | Portable without slash? | Who uses it |
| --- | --- | --- | --- |
| **A. Always-on pointer** | Root `AGENTS.md` (or `GEMINI.md` / `CLAUDE.md`) says “before doing X, read skill Y / state file Z”. | Yes, if the harness loads `AGENTS.md`. | agents.md standard; Codex; Cursor; Copilot; OpenCode; Kimi; Claude; Aider with `read:`. |
| **B. Catalog + description match** | Each `SKILL.md` `description` is in the system prompt. Model *may* invoke the skill when the user task matches. | Yes, if skills are in a scanned path (`.agents/skills/`). No guarantee it fires on turn 1. | Agent Skills spec. Superpowers Codex install after they dropped the bootstrap CLI. |
| **C. Session-start injection** | Hook / plugin / import **forces** the bootstrap skill into the first turn, before the model answers. | **No.** Per-harness plugins. This is why Superpowers “just has Superpowers”. | Superpowers on Claude, Kimi, Gemini, Pi, OpenCode, Muse, Antigravity, Hermes. |

The pattern “one skill reads a state file and tells the agent the next phase” is **layer B + a file**. It is not layer C. Treating Superpowers as proof that B is enough is a category error — Superpowers spent 2025–2026 building C for every harness, and still documents C as the acceptance test.

### 1.2 obra/superpowers — the reference implementation

Repo: <https://github.com/obra/superpowers> (v6.4.2 as of 2026-09-25). ~296k stars. Skills are ordinary `skills/<name>/SKILL.md`. The methodology is a **chain of skills**, not a single orchestrator that encodes every phase:

1. `brainstorming` → 2. `using-git-worktrees` → 3. `writing-plans` → 4. `subagent-driven-development` **or** `executing-plans` → 5. `test-driven-development` → 6. `requesting-code-review` → 7. `finishing-a-development-branch`.

**Bootstrap skill** (`skills/using-superpowers/SKILL.md`):

- `description`: “Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions”
- Hard rule: if there is even a 1% chance a skill applies, invoke it **before** clarifying questions or exploring the repo.
- Subagents skip it: “If you were dispatched as a subagent to execute a specific task, ignore this skill.”
- Speaks in actions, then points at per-harness tool maps (`references/codex-tools.md`, etc.).
- Precedence: user instructions (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, direct requests) **beat** skills.

**How a cold session actually gets that skill (this is the non-portable part):**

| Harness | Bootstrap mechanism (first-party in the Superpowers repo) |
| --- | --- |
| Claude Code | Plugin SessionStart hook. Jesse Vincent’s 2025-10-09 post shows the injected block: “You have Superpowers. **RIGHT NOW, go read**: …/using-superpowers/SKILL.md”. Hook was later set `async: false` so it lands before turn 1 (v4.3.0). |
| Kimi Code | `.kimi-plugin/plugin.json`: points at `skills/`, loads `using-superpowers` via `sessionStart.skill`, maps “Dispatch a subagent” → `Agent`. Docs: `docs/README.kimi.md`. Fresh `/new` session required after install. |
| Gemini CLI | Root `GEMINI.md` is literally `@./skills/using-superpowers/SKILL.md` plus the Gemini tool map. Extension install: `gemini extensions install https://github.com/obra/superpowers`. |
| OpenCode | JS plugin. V2: `ctx.session.hook("context")` injects bootstrap; re-injects after compaction. Child/delegated sessions **do not** get the controller bootstrap. Docs: `docs/README.opencode.md`. |
| Pi | Package extension injects bootstrap at session start **and again after compaction**. Native skills; no Skill-tool shim. |
| Muse / Antigravity | Native SessionStart hook. Acceptance prompt: “Let's make a react todo list” must auto-trigger `brainstorming` before any code. |
| Codex | **Used to** inject via a bootstrap CLI into `~/.codex/AGENTS.md`. **v4.2.0 (2026-02) removed it.** Now: native skill discovery via `~/.agents/skills/superpowers` symlink / official plugin marketplace. Old installs must delete the bootstrap block from `~/.codex/AGENTS.md`. |
| Hermes | Plugin install. **No post-compaction hook** — a long session that compact-drops the first turn loses the bootstrap. Superpowers tells you to start a fresh session. |
| Cursor | Official `/add-plugin superpowers`. Community fork `chauchakching/superpowers-cursor` still copies a `sessionStart` hook + `.cursor/rules` because catalog-only was not enough for them. |

**Contributor rule (RELEASE-NOTES v5.1.0):** “most past new-harness integrations copied skill files or wrapped with `npx skills` instead of loading the using-superpowers bootstrap at session start.” Required evidence is a transcript of the react-todo-list prompt auto-triggering `brainstorming` in a **clean** session.

That is the strongest open-source evidence we have: **skills on disk are not sufficient; injection is.** Codex is the interesting exception — they now bet that native skill discovery (layer B) plus a trigger-only description is enough, and they deleted the AGENTS.md bootstrap.

**State files inside Superpowers (the part that *is* portable):**

- Plans: `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` with checkbox tasks. Header **requires** the next skill by name (`subagent-driven-development` or `executing-plans`).
- SDD workspace: gitignored `/.superpowers/sdd/<plan>/` holding `progress.md` ledger, task briefs, reports. After compaction, “trust the ledger and `git log` over your own recollection.”
- `executing-plans` is the **no-subagent / cheaper** path: load plan, execute inline, one final review. Explicitly: “Tell your human partner that Superpowers works much better with access to subagents (Claude Code, Codex CLI, Codex App, Copilot CLI, and Gemini CLI all qualify)… If subagents are available, use subagent-driven-development instead.”

So: Superpowers **does** implement “read a repo state file → know where you are → what next → where outputs go.” The state file is the plan + ledger. The orchestrator is split across `using-superpowers` (always) + `writing-plans` / `executing-plans` / `subagent-driven-development` (phased). The thing that makes it fire on turn 1 is not the state file.

### 1.3 mattpocock/skills — router + tracker, not a bootstrap

Repo: <https://github.com/mattpocock/skills>. Philosophy: small composable skills; user-invoked skills orchestrate; model-invoked skills hold discipline.

- **`ask-matt`**: “A router over the user-invoked skills.” Marked `disable-model-invocation: true`. Expects `/ask-matt`. Without slash, this skill **will not auto-fire**.
- **`wayfinder`**: multi-session planning as a **map of decision tickets on an issue tracker** (GitHub / GitLab / local markdown under `.scratch/`). One ticket per session. State is the tracker, not a SKILL.md. This is the closest cousin to “read a state file, tell the agent the next phase” — except the state is issues, and a human (or the skill, once invoked) picks the frontier ticket.
- **`setup-matt-pocock-skills`**: writes `docs/agents/issue-tracker.md` etc., and a short `## Agent skills` block into **whichever of `CLAUDE.md` / `AGENTS.md` already exists**. Known gap (aihero.dev): if `CLAUDE.md` exists, Codex never sees the block. Pointers, not procedures — matches agents.md hygiene.
- Issue **#197** proposes a `skill-orchestrator` that *recommends* a chain and stop points; it is a discussion, not shipped methodology.
- Retro skill: “`CLAUDE.md`/`AGENTS.md` … should be used incredibly sparingly, usually only for navigation pointers to other files.”

Matt’s set is evidence that **file/tracker state + a router skill** is a working pattern, and also evidence that **user-invoked skills without slash are a problem** — the whole “main flow” is documented as `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`.

### 1.4 Other collections (weaker, still useful)

- **wshobson/agents** (`docs/harnesses.md`): generates **per-harness trees** (`.claude/`, `.codex/`, `.opencode/commands/`, `.pi/prompts/`). Confirms there is still no write-once command layer; the portable unit is the skill, the rest is transformed.
- **OpenCode rules**: `AGENTS.md` can *tell* the model to Read `@docs/foo.md` on demand. That is poor-man’s progressive disclosure when there is no skill scanner — exactly Aider’s situation.

### 1.5 Verdict for this playbook

| Claim | Evidence | Implication |
| --- | --- | --- |
| “A skill that reads a state file can drive phases” | Superpowers plans + SDD ledger; mattpocock wayfinder map | **Yes, as a method.** Put phase, next skill, and output path in a small markdown file the orchestrator is told to Read. |
| “Any harness will follow that skill from a cold session with nobody explaining” | Superpowers requires session-start injection and an acceptance test; Codex deleted injection and bets on catalog; Hermes loses it on compact | **Unproven without the pilot.** Layer B may work on Kimi/Codex/Cursor/Gemini/OpenCode if `.agents/skills/` is populated and the description is a blunt trigger. It will not work on Aider without `read:`. It will not work on Claude Code unless `.claude/skills/` is linked (see sibling research). |
| “We can skip hooks/plugins” | This repo’s map: no harness-only wiring in canonical skills | Correct as policy. Then **pilot must treat auto-trigger as a hypothesis**, and ship a pasteable command card as the escape hatch. |

---

## 2. Sub-agent portability

“Can skill/instruction text trigger a subagent?” means two different things:

1. **Harness runtime:** is there a spawn tool at all?
2. **Instruction following:** if a `SKILL.md` says “dispatch a subagent / spawn one agent per task”, will the model call that tool without a human `/` command?

### 2.1 Matrix (first-party)

| Harness | Spawn equivalent | How the model is supposed to start it | Custom agent files | Skill text can request it? | Fallback if missing |
| --- | --- | --- | --- | --- | --- |
| **Claude Code** | Task tool; built-ins Explore / Plan / general-purpose; `.claude/agents/*.md` | Auto when description matches; user `@agent`; skill frontmatter `context: fork` + `agent:` (**Claude-only**, not in Agent Skills spec) | Yes | Yes. Official skills page documents “run skills in a subagent”. Subagents do **not** inherit parent skills unless listed in agent `skills:` (full body injected at start). | N/A |
| **Kimi Code** | `Agent` tool (default auto-allow). Built-ins `coder`, `explore`, `plan`. Nested spawn off unless custom `subagents:` allowlist. | Main agent schedules automatically; user can say “Use explore to map files…”. Approval unless allow-rule. | `.kimi-code/agents/`, `.agents/agents/`, `~/.agents/agents/` | Superpowers maps “Dispatch a subagent” → `Agent`. Official: skills influence sub-agent behavior; `coder` may invoke skills. | Same session |
| **OpenAI Codex CLI** | Subagent workflows **on by default** in current releases (`agents.enabled` default true). Tools historically `spawn_agent` / `wait_agent` / `close_agent` (Superpowers still documents `[features] multi_agent = true` for older builds). Built-ins `default`, `worker`, `explorer`. | “Ask for subagents or parallel agent work directly. **Codex can also follow applicable `AGENTS.md` or skill instructions that request delegation.**” Ultra/Work may delegate proactively. | `~/.codex/agents/*.toml` or `.codex/agents/` (`name`, `description`, `developer_instructions`) | **Yes, documented.** This is the most important 2026 change for us. | Inline; Superpowers `executing-plans` |
| **Cursor** | Task tool. Built-ins Explore, Bash, Browser (automatic). Custom `.cursor/agents/*.md` (also reads `.claude/agents/`, `.codex/agents/`) | Auto from description (“use proactively”); explicit `/verifier` or “use the verifier subagent”; parallel = multiple Task calls in one message | Yes | Yes, if description is good. Forum report: a skill that “commands” subagent use is sometimes ignored — treat as unreliable. Nested spawn since 2.5, depth-capped. | Skill instead of subagent for one-shot work |
| **Gemini CLI** | Subagents exposed **as tools of the same name**. Built-ins `codebase_investigator`, `cli_help`, `generalist`; `browser_agent` off by default. | Auto from description; force with `@codebase_investigator …` (injects a system note). `/agents` to manage. | `.gemini/agents/*.md` | Yes, via description or `@`. **Subagents cannot call other subagents** (recursion protection even with `tools: *`). Unpaid Gemini CLI → Antigravity CLI as of 2026-06-18. | `generalist` as isolated same-capability worker |
| **OpenCode** | `task` tool; agents with `mode: subagent`. Builtin `general` cannot launch further subagents. `subagent_depth` in config. | Commands with `subtask: true` force a subagent. Superpowers maps “Subagent (general-purpose)” → `task` with `subagent_type: "general"`. | `.opencode/` markdown / JSONC agents | Yes if the skill says “dispatch a subagent” and the plugin mapped it; a raw SKILL.md without mapping is hoping the model knows `task`. | Primary agent runs the work |
| **Aider** | **None.** Pair-programmer, one conversation. | — | — | No | `/read` files; `read:` in `.aider.conf.yml` |

Sources: Claude [sub-agents](https://code.claude.com/docs/en/sub-agents), [skills/slash-commands](https://code.claude.com/docs/en/slash-commands); Codex [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) (URL `developers.openai.com/codex/subagents` redirects here); Kimi [agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html), [tools](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/tools.html); Cursor [subagents](https://cursor.com/docs/subagents); Gemini [subagents](https://geminicli.com/docs/core/subagents/); OpenCode [agents](https://opencode.ai/docs/agents/), [v2 agents](https://opencode.ai/v2/docs/agents/); Aider has no equivalent page.

### 2.2 What skill authors should write (portable)

Superpowers’ choice, which we should copy:

- In the skill body: “Dispatch a subagent (general-purpose): …” / “If your harness has no subagent tool, do the task inline in this session.”
- **Not:** `Task(subagent_type=…)`, `Agent`, `spawn_agent`, `@codebase_investigator`, `context: fork`.
- Per-harness tool maps belong in adapters, not in canonical `SKILL.md`.

Official Codex language is the green light we needed: **skill/AGENTS.md text that requests delegation is a supported trigger**, not undefined behavior. That does not make it reliable — only that OpenAI intends the model to obey it.

Claude `context: fork` / `agent:` and Kimi `disableModelInvocation` / `type: flow` are **vendor extensions**. Forbidden in this playbook’s canonical skills (sibling research already locked that).

### 2.3 Fallback when there is no spawn tool

Already designed in Superpowers: `executing-plans` = one context, follow the plan, one review at the end. For this playbook: the mini-orchestrator’s last instruction should be “if you cannot dispatch, perform the next skill’s method yourself and write the deliverable.” Aider is the existence proof that this path must work.

Do not generate `.claude/agents/` or `.codex/agents/*.toml` as part of extraction. Those are adapters for later, if a human actually uses that harness daily.

---

## 3. Prompt / command reuse — no portable convention

There is **no** cross-harness command-file standard. Vendors are converging on **Agent Skills** (`SKILL.md`) and treating command markdown as a legacy slash UX.

| Vendor | Old / parallel command files | 2026 status | Shared via git? |
| --- | --- | --- | --- |
| **Claude Code** | `.claude/commands/*.md` → `/name` | **Merged into skills.** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`. Commands still work. Skills add supporting dirs + invocation control. | Project commands yes |
| **Codex** | `~/.codex/prompts/*.md` → `/prompts:name` | **Deprecated.** Docs: “Custom prompts are deprecated. Use skills… Custom prompts require explicit invocation and live in your local Codex home… **so they’re not shared through your repository.**” Placeholders `$1`–`$9`, `$ARGUMENTS`, `$NAME=`. Top-level md only, no subdirs. | **No** (home dir) |
| **Cursor** | `.cursor/commands/[command].md` (since 1.6) | Migrating **to skills**. Built-in `/migrate-to-skills` converts slash commands. Skills invoked with `/skill-name` or `@`. CLI: pick a skill from `/` for one message, or Option+Enter as a Custom Mode. | Project commands yes |
| **OpenCode** | `.opencode/commands/*.md` or `command` in `opencode.json` | Still first-class. `$ARGUMENTS`, `$1`, `` !`shell` ``, `@file`. Optional `agent`, `subtask: true`, `model`. | Yes |
| **Kimi Code** | No separate commands tree | Skills **are** the slash UX: `/skill:code-style`. Also auto-invoke from `description` / `whenToUse`. Extra fields (`type`, `arguments`, `disableModelInvocation`) are Kimi-only. | Skills in `.agents/skills/` yes |
| **Gemini CLI** | `/skills` is a **management** command, not user prompt files | Skills live in `.gemini/skills/` or `.agents/skills/`. | Skills yes |
| **Aider** | No commands, no skills scanner | Conventions file via `/read` or `read:` in `.aider.conf.yml`. | If you commit the file |

**Portable prompt = `SKILL.md` in a scanned skills directory.** That is the Agent Skills spec. Everything else (`$ARGUMENTS`, `!`, `context: fork`, `subtask: true`) is an adapter.

**Implication for option 丙 (command cards):** a folder of plain markdown “paste this into any agent” still works everywhere, including Aider, and does not require a scanner. It is the honest no-magic driver. It is also what Codex custom prompts used to be, except Codex kept them out of the repo on purpose. If we keep cards, put them in-repo as human-facing `commands/*.md` **without** claiming any harness will auto-load them.

---

## 4. `AGENTS.md` as driver — practical limits

### 4.1 What the standard actually is

<https://agents.md/> — stewarded by the Agentic AI Foundation (Linux Foundation). Markdown, **no required fields**. Complementary to README. Closest file to the edited path wins; user chat overrides everything. Nested files are expected in monorepos (OpenAI’s own repo cited as 88 files).

Supported (from the standard’s own logo wall + first-party docs): Codex, Cursor, Copilot, Amp, Factory, Devin, Goose, Warp, Zed, OpenCode, Gemini CLI (via `context.fileName`), Aider (`read:`), VS Code, Kimi, Claude Code (on its own or beside `CLAUDE.md`).

### 4.2 Hard caps and silent failure

| Limit | Source | What happens |
| --- | --- | --- |
| Codex combined project docs **32 KiB** (`project_doc_max_bytes`) | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | “stops adding files once the combined size reaches the limit”. Empty files skipped. Nested walk root → cwd. |
| Truncation is **silent** | openai/codex#7138, #13386 | Instructions after the cut are simply not in the prompt. Community tool `dropped` exists because people did not notice. Default 32 KiB ≈ 600–800 lines; raise via config or split nested. |
| Claude standing instructions | [Memory](https://code.claude.com/docs/en/memory) | Loaded every session. “Claude treats them as **context, not enforced configuration**.” “The more specific and concise your instructions, the more consistently Claude follows them.” Hooks enforce; markdown does not. |
| Kimi | [Agents](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html) | Workspace `AGENTS.md` is injected as `${agents_md}` **reference data**. A project `agents/*.md` with `override: true` **is** the system prompt (different, more dangerous). |
| OpenCode | [Rules](https://opencode.ai/docs/rules/) | `AGENTS.md` wins over `CLAUDE.md` if both exist. Does **not** auto-follow `@file` references unless you instruct it to Read, or list files in `opencode.json` `instructions`. |
| Gemini | agents.md FAQ | Default file is `GEMINI.md`. `{"context":{"fileName":"AGENTS.md"}}` in `.gemini/settings.json` to unify. |
| Aider | [Conventions](https://aider.chat/docs/usage/conventions.html) + agents.md FAQ | `read: AGENTS.md` in `.aider.conf.yml`. No scanner, no subagents. |

### 4.3 Instruction-following reality (not just bytes)

- **Length vs obedience:** Anthropic’s own memory page is the first-party statement: shorter, more specific standing instructions are followed more. Matt Pocock’s authoring rule is the same: AGENTS.md = navigation pointers.
- **Compaction kills bootstrap:** Superpowers SDD ledger exists because controllers re-did finished work after compact. Hermes explicitly loses Superpowers after compact. Any orchestrator that only lives in the conversation will drift. **The state file is the recovery map.**
- **Precedence fights:** Superpowers: user AGENTS.md beats skills. If AGENTS.md says “don’t use TDD” and a skill says “always TDD”, the file wins. Keep playbook rules in the skill, keep the root file as a pointer, or they will contradict.
- **Wrong file, wrong harness:** setup-matt-pocock-skills writing `## Agent skills` into `CLAUDE.md` when Codex is the daily driver is a documented miss. This playbook: **only `AGENTS.md`**, no twin `CLAUDE.md` (already decided in the conventions research).
- **Catalog pressure** (sibling research): Codex skill list 8k chars; Zed 50 KB catalog. 80 fat descriptions will be truncated independently of the 32 KiB AGENTS.md cap.

### 4.4 What root `AGENTS.md` should contain for orchestration

Safe (all first-party-aligned):

- One paragraph: this repo is a portable skill playbook.
- Where skills live (`skills/` canonical, `.agents/skills/` discovery).
- “Match the user task to a skill description; follow that SKILL.md; do not invent a parallel method.”
- Pointer to the **state/status file** the mini-orchestrator owns, and the output directory (`deliverables/`).
- Pointer to Linker facts in `~/Documents/New` (read, don’t copy) — already a map constraint.
- Example rule: skill examples are scaffolds, never quote into deliverables.

Unsafe:

- Full phase machines.
- Tool IDs.
- Copies of skill bodies.
- Anything that only matters after the 32 KiB cut.

Aim well under 32 KiB; a few hundred lines is the design point already in the conventions brief.

---

## 5. How a cold session is supposed to run (without slash)

This is the stack the **pilot slice** must prove, not assume.

```
harness starts
  → loads AGENTS.md (if it knows how)
  → lists skill name+description from .agents/skills/ (if it scans)
  → user says something like “audit this landing page” / “do the next marketing step”
  → model matches description → loads orchestrator SKILL.md
  → orchestrator Reads state file
  → announces phase, next method skill, output path
  → loads that method skill (or does the work inline)
  → writes deliverable + updates state file
```

Failure modes to expect (from the evidence above):

1. **No scan:** Claude Code without `.claude/skills/` symlink; Aider without `read:`; Gemini untrusted workspace.
2. **No match:** orchestrator description too vague, or catalog truncated, or `disable-model-invocation` equivalent hiding it.
3. **Match but skip:** Superpowers’ entire red-flag table exists because models rationalize “this is a simple question / I’ll explore first.” Trigger-only descriptions + a brutal first paragraph are the known mitigation (Superpowers “Description Trap”: putting the workflow *in the description* made Claude follow the summary and skip the body).
4. **Match, then forget after compact:** no ledger → re-does phase 1.
5. **Match, tries `Task`/`Agent` by name, tool missing:** must have inline fallback in the skill text.
6. **AGENTS.md truncated:** last sections (often “where outputs go”) vanish. Put the state-file pointer **near the top**.

---

## 6. Mapping onto this repo’s 甲 / 乙 / 丙 options

From `wayfinder/tickets/orchestration-workflow-form.md`. Evidence, not a ruling (ruling waits on the pilot).

| Option | What the evidence says |
| --- | --- |
| **甲. Wayfinder tickets** | Proven by mattpocock/wayfinder and by *this* playbook’s own map. Best for work bigger than one session. Cost: even small SEO tasks need a ticket. Fits “progress is visible”. Does not by itself make a cold marketing session do the next SEO audit. |
| **乙. Orchestrator self-drive** | Proven **as a method** (Superpowers plans/ledger). Proven **as auto-start** only with session-start injection, which we are not shipping. Layer-B auto-start is what the pilot must measure. Drift without a ledger is documented. |
| **丙. Command cards** | The only mechanism that works in *every* harness including Aider: human pastes markdown. Codex deprecated in-home prompts *because* they were not repo-shared; in-repo cards invert that. No auto-trigger. |

Likely end state after a real pilot (prediction, not a lock): **乙 for harnesses that auto-load the orchestrator, 丙 as the printed fallback, 甲 for multi-session campaigns.** Do not encode that mix until the matrix is filled in.

---

## 7. Pilot slice — what must be tested empirically

The pilot ticket already requires: min skeleton + 2 skills + ≥2 harnesses, cold session, only AGENTS.md, a real file in `deliverables/`. Below is the **instrumented** checklist so the orchestration-form ticket can actually decide.

### 7.1 Fixture (keep tiny)

- `AGENTS.md` ≤ ~80 lines, **state-file pointer in the first screen**.
- `skills/mini-orchestrator/SKILL.md` — description starts with “Use when starting any session in this repo, or when the user wants the next marketing/SEO/content step”. Body: Read `state/status.md` → print phase → name the method skill → name output path → “if you have a subagent tool, you may dispatch; otherwise do it inline” → update the state file when done.
- `skills/<method>/SKILL.md` — one independent method (copy or SEO-audit lite) that writes **one** real artifact under `deliverables/`.
- `.agents/skills/<name>` symlinks. **Do not** add Claude `context: fork`, Kimi `whenToUse`, or `$ARGUMENTS`.
- `state/status.md` with explicit `phase`, `next`, `output_dir`. Start in `phase: 0` / next = method skill.

### 7.2 Harness matrix (fill one row per CLI)

Required: **kimi** + at least one of `claude`, `codex`, `cursor-agent`, `gemini`, `opencode`. Optional: Aider as the no-spawn / no-scan control.

For each harness, a **new** session, cwd = playbook root, prompt **only**:

> Do the next step this repo is set up to do. Do not ask me to explain the repo.

Record:

| # | Question | Pass looks like |
| --- | --- | --- |
| 1 | Did it load `AGENTS.md` without being told? | Quotes or follows the pointer. |
| 2 | Did it see the orchestrator in the skill catalog? | Mentions it / Skill-tool call / equivalent. |
| 3 | Did it **invoke** the orchestrator before exploring or writing? | Superpowers-style “Using mini-orchestrator…”. Fail = jumps to editing. |
| 4 | Did it Read `state/status.md`? | Tool call. |
| 5 | Did it then load the **method** skill (not invent a process)? | Second skill load, or a Read of that SKILL.md. |
| 6 | Did a real deliverable land in `deliverables/`? | File exists, not empty, not a copy of the skill’s example. |
| 7 | Did it update the state file? | `phase`/`next` changed. |
| 8 | Subagent: did it try to spawn? Did the spawn tool exist? Did inline fallback work if not? | Three-way: spawned / inline / confused. |
| 9 | Slash: did it wait for `/something`? | Fail if it stalled asking for a command. |
| 10 | Compaction (optional, kimi/claude/codex): mid-run `/compact` or equivalent, then “continue”. | Resumes from **state file**, not from hallucinated progress. |

Second prompt, even colder: **empty user message equivalent** — “hello” — should *not* run the whole pipeline. The orchestrator must still gate on a real task. (Catches “description = starting any conversation” overfiring, which Superpowers wants and we may not.)

### 7.3 Negative tests (cheap, high value)

- Remove `.agents/skills/` and retry on Codex/Kimi: expect catalog miss; `AGENTS.md` should still point at `skills/…/SKILL.md` for a Read. If even that fails, 乙 is dead on that harness without an adapter.
- On Claude Code, **without** `.claude/skills/` symlink: confirm the sibling research (Claude does not document `.agents/skills/`).
- Put a 40 KiB blob at the **end** of `AGENTS.md` and a one-line “MUST write MAGIC=7f3a to deliverables/canary.txt” at the bottom; on Codex, check whether the canary is followed. Documents truncation in *this* repo rather than citing GitHub issues.

### 7.4 What the orchestration ticket should accept as evidence

A table with harness rows and questions 1–10. No narrative “it felt like it worked.” If kimi passes 1–7 and 9, 乙 is viable as the daily driver on the main harness. If only 丙 (paste the orchestrator body) passes, lock 丙 for v1 and keep 乙 as a later adapter.

---

## 8. Source list

### Superpowers (pattern + bootstrap)

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/using-superpowers/references/codex-tools.md
- https://github.com/obra/superpowers/blob/main/docs/README.kimi.md
- https://github.com/obra/superpowers/blob/main/docs/README.opencode.md
- https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md
- https://blog.fsck.com/2025/10/09/superpowers/ (author; hook injection quote)

### mattpocock

- https://github.com/mattpocock/skills
- https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md
- https://github.com/mattpocock/skills/issues/197 (orchestrator proposal; not shipped)
- https://www.aihero.dev/skills-setup-matt-pocock-skills (CLAUDE.md vs AGENTS.md gap)

### Harness docs — subagents / skills / commands / AGENTS.md

- AGENTS.md standard: https://agents.md/
- Codex AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Codex subagents: https://learn.chatgpt.com/docs/agent-configuration/subagents (canonical for developers.openai.com/codex/subagents)
- Codex custom prompts (deprecated): https://learn.chatgpt.com/docs/custom-prompts
- Codex silent truncation: https://github.com/openai/codex/issues/7138 , https://github.com/openai/codex/issues/13386
- Claude subagents: https://code.claude.com/docs/en/sub-agents
- Claude skills / commands merge: https://code.claude.com/docs/en/slash-commands
- Claude memory / AGENTS.md: https://code.claude.com/docs/en/memory
- Cursor subagents: https://cursor.com/docs/subagents
- Cursor skills + command migration: https://cursor.com/help/customization/skills
- Cursor CLI `/` skills and AGENTS.md: https://cursor.com/docs/cli/using
- Gemini subagents: https://geminicli.com/docs/core/subagents/
- Kimi agents: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents.html
- Kimi skills: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills
- Kimi Agent tool: https://www.kimi.com/code/docs/en/kimi-code-cli/reference/tools.html
- OpenCode agents: https://opencode.ai/docs/agents/ , https://opencode.ai/v2/docs/agents/
- OpenCode commands: https://opencode.ai/docs/commands/
- OpenCode rules / AGENTS.md: https://opencode.ai/docs/rules/
- Aider conventions: https://aider.chat/docs/usage/conventions.html

### Sibling brief (skill layout / scan paths / 32 KiB already noted)

- `wayfinder/research/skill-conventions-best-practices-2026-10.md`

### Not used as authority

- Blog roundups that claim Codex “never” auto-spawns (superseded by current OpenAI subagents page).
- MorphLLM / third-party “codex task run --mode subagents” recipes that do not match the current CLI.
- Superpowers Cursor unofficial fork, except as evidence that catalog-only was insufficient for that author.

---

## 9. Gaps (do not block the pilot)

- Whether Antigravity CLI (Gemini unpaid successor) keeps `.agents/skills/` and subagents — Gemini docs still describe them; Superpowers has an Antigravity install path.
- Exact Codex spawn tool names in the *current* CLI vs Superpowers’ `spawn_agent` note — the OpenAI page describes the workflow, not the tool JSON. Pilot will see the tool list.
- Claude Code still not documented as scanning `.agents/skills/` — adapter remains required (sibling brief).
- No first-party eval of “AGENTS.md pointer vs session-start hook” success rates. Superpowers’ required transcript is the closest, and it tests the hook, not the pointer.
- Instruction-following of long skills after compaction is known-bad; we did not re-run those evals here.
