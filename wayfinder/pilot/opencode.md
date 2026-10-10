# Pilot run: opencode

- **harness:** OpenCode CLI (`opencode`)
- **version:** `opencode v2.0.24`
- **binary:** `/Users/chesterjohn/.opencode/bin/opencode` (Mach-O arm64)
- **model (work):** `deepseek/deepseek-v4-pro` (`-m`; user config default `xai/grok-4.6` is auth-dead)
- **date:** 2026-10-10 13:20–13:23 CST
- **driver:** subagent, harness = opencode
- **copy:** `/tmp/de-linker-accept-opencode/` (rsync `-a --exclude .git` from `/Users/chesterjohn/Documents/de-linker-playbook/`; symlinks preserved). Session cwd resolved to `/private/tmp/de-linker-accept-opencode`.
- **original repo:** mutated only under `wayfinder/pilot/` (this log + copied ledger)
- **git:** not run against the copy (copy has no `.git`; OpenCode did not refuse)
- **sessions:** S1 `ses_edbbd9b54ffeYGCvTUgKHcjNM3` (`accept-s1-cold`); S3 `ses_edbbbbedcffees30dOOiBrw9ks` (`accept-s3-greeting`). Fresh sessions (no `-c`/`-s`).

## Verdict

**PASS** (S1 **PASS**, S3 **PASS**).

S1: one cold `opencode run` with only the next-step prompt completed the playbook loop unassisted: followed injected `AGENTS.md` (read ledger then `marketing-orchestrator/SKILL.md`), announced phase 0 then did it, expanded `~` to `$HOME` for `product_context`, wrote three statements, rewrote the copy ledger to `phase: 1` / `method_skill: marketing-positioning` / `output_dir: deliverables/marketing/01-foundation/`, and stopped. No slash-command wait. No web crawl. Auth after the default-model miss is not a FAIL.

S3: second fresh session, prompt `你好`, read `state/status.md` only, recapped phase / next / output path, **checksum of the copy unchanged**.

Judge the loop, not the phase. Copy ledger started at phase 0; advancing 0→1 (CONTEXT.md + three statements, no file under `deliverables/`) is in-spec. Phase 1 foundation work was **not** started.

## Headless / permission flags (portability)

From `opencode --help` / `opencode run --help` (v2.0.24):

| Need | Flag |
| --- | --- |
| Non-interactive / batch | `opencode run [flags] [<message...>]` (top-level `opencode [PROMPT]` is TUI) |
| Never hang on permission prompts | `--auto` — “Auto-approve permissions that are not explicitly denied.” Default `build` agent: `action: *` allow, but `external_directory` on `*` is **ask**. Reading `~/Documents/New/CONTEXT.md` is outside the copy → **`--auto` required** for unattended phase 0. Writes inside the copy do not need a second flag. |
| Model | `-m` / `--model provider/model` or `provider/model#variant` |
| Trace tool use | `--format json` (NDJSON events: `step_start` / `tool_use` / `text` / `step_finish`; choices: `default`, `json`) |
| Cold start | omit `-c` / `--continue` and `-s` / `--session` |
| Resume | `-c` last session; `-s <id>` continue or create |
| Fork | `--fork` (with continue) |
| Isolate from user’s background service | `--standalone` (private server; used here) |
| Working root | **cwd** (no Codex-style `-C`). Top-level usage lists `[<directory>]` for the TUI; `run` treats extra args as the message. |
| Session title | `--title` |
| Attach file | `-f` / `--file` |
| Show thinking | `--thinking` |
| Agent | `--agent` (default `build`; `debug agents` also lists `explore`, `compaction`, …) |
| Stdin | not required; `</dev/null` used anyway |
| No git in copy | **no extra flag** (unlike Codex `--skip-git-repo-check`) |
| No Claude-style names | no `--permission-mode`, `--yolo`, `acceptEdits`, `--dangerously-skip-permissions` |

User `~/.config/opencode/opencode.json`: `model: xai/grok-4.6`, `small_model: deepseek/deepseek-flash`. `opencode auth list` shows stored creds for OpenCode Go, AIHubMix, DeepSeek, Kimi For Coding, OpenAI, OpenRouter, xAI (OAuth + named slots). Default xAI OAuth is **broken** (`invalid_grant`).

## Auth probe (not counted as an attempt)

Default model (cwd `/tmp`):

```bash
cd /tmp
opencode run --standalone --auto --format json --title "accept-auth-probe" \
  "Reply with only the word PONG."
```

Exit 1, ~4.05s. JSON:

```json
{"type":"error","error":{"type":"provider.auth","message":"xAI request failed (400): {\"error\":\"invalid_grant\",\"error_description\":\"Invalid or unknown refresh token\"}"}}
```

Stored-provider retry:

```bash
cd /tmp
opencode run --standalone --auto --format json -m deepseek/deepseek-flash \
  --title "accept-auth-deepseek-flash" \
  "Reply with only the word PONG."
```

Exit 0, ~4.64s. Text part `"PONG"`. Same DeepSeek stored login used for work as `-m deepseek/deepseek-v4-pro`.

## Headless commands actually run

S1 (scored cold start):

```bash
cd /tmp/de-linker-accept-opencode
opencode run \
  --standalone --auto --format json \
  -m deepseek/deepseek-v4-pro \
  --title "accept-s1-cold" \
  "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  < /dev/null
```

Wall **85.13s** (05:21:32Z–05:22:57Z), exit 0. Session `ses_edbbd9b54ffeYGCvTUgKHcjNM3`. Export: `outcome: succeeded`, `cost: 0.055`, tokens input 47612 / output 2178 / reasoning 5387 / cache-read 395392.

S3 (scored greeting, second fresh session):

```bash
cd /tmp/de-linker-accept-opencode
opencode run \
  --standalone --auto --format json \
  -m deepseek/deepseek-v4-pro \
  --title "accept-s3-greeting" \
  "你好" \
  < /dev/null
```

Wall **7.32s** (05:23:34Z–05:23:41Z), exit 0. Session `ses_edbbbbedcffees30dOOiBrw9ks`.

Checksum of the copy (`find` + `shasum -a 256`, excluding `.opencode/` which never appeared): **identical** before vs after S3. Only copy mutation in the whole test is `state/status.md` during S1 (`29261b27…` → `9f453dfd…`). Original repo `state/status.md` left at phase 0 (`29261b27…`).

## Attempts

1. S1 work prompt above. Completed under the 10-minute cap; not killed. Did not start a large/network task.
2. Not used (no work retry). S3 is a separate scenario, not a second S1 attempt.

## Checklist

| # | Item | Result |
| --- | --- | --- |
| ① | Actively read `AGENTS.md` | **YES (injected, not Read).** Server log watches `/private/tmp/de-linker-accept-opencode/AGENTS.md` plus `~/.config/opencode/AGENTS.md`. No `read` of `AGENTS.md`. First tools still match 本仓库: `state/status.md` then `skills/marketing-orchestrator/SKILL.md`. |
| ② | Found skill dir / orchestrator | **YES.** Direct `read` of canonical `skills/marketing-orchestrator/SKILL.md` (not a Skill() tool — OpenCode has none). `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator` intact after rsync. Global skill dirs also watched (`~/.agents/skills`, `~/.zcode/skills`, `~/.claude/skills`, `~/.config/opencode/skills`); agent still picked the repo orchestrator. |
| ③ | Called orchestrator before writing | **YES.** Tools 1–2 = ledger + orchestrator. All `edit` came after CONTEXT + dependency-graph. Announced phase 0 in an assistant text part before writing. |
| ④ | Read `state/status.md` | **YES** — first `read`. |
| ⑤ | Actually followed the method skill (did not invent a flow) | **YES for the loop.** Phase 0 contract is 只读 `product_context` + three statements; it did that. Did **not** open `skills/marketing-profile/SKILL.md` even though the starting ledger had `method_skill: marketing-profile` (orchestrator table: open it when a profile is needed). Peeked at `marketing-positioning/SKILL.md` + `references/dependency-graph.md` then **stopped** instead of running phase 1. No parallel invented pipeline. |
| ⑥ | Non-empty deliverable under `deliverables/`; not skill-example paste; no invented product numbers | **N/A file / YES loop.** Phase 0 不落盘. Copy `deliverables/` still only `.gitkeep`. Three statements in the assistant reply; CONTEXT.md not copied into the playbook copy. Product names/certs in the statements trace to `~/Documents/New`, not skill examples. |
| ⑦ | Wrote ledger (phase / next / 已完成) | **YES.** YAML + 「当前」 table + 「已完成」. `phase: 0` → `1`, `phase_name: 基础`, `method_skill: marketing-positioning`, `output_dir: deliverables/marketing/01-foundation/`, `next` = parallel positioning + competitor-intelligence then pricing. Artifact: `wayfinder/pilot/opencode/status.md`. |
| ⑧ | Subagent behavior (harness-specific tool names) | **No spawn.** Tools: `read` ×8, `shell` ×2 (`ls` of `~/Documents/New` / `fact-base/`), `edit` ×3 (same ledger). Inline, matching orchestrator “else do it inline”. |
| ⑨ | Idled waiting for a slash command | **NO.** Never asked for `/…`. Skills via `read` of `SKILL.md`, not slash. |
| ⑩ | Other anomalies | See below. `~` expansion **correct.** |

Copy tree after rsync (symlinks intact):

- `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator`
- `.agents/skills/marketing-copywriting` → `../../skills/marketing-copywriting`

### ⑩ other / portability notes

- **Default model is not runnable** on this host until xAI OAuth is refreshed. Portable unattended OpenCode needs an explicit `-m` to a stored provider that still authenticates (here DeepSeek).
- **`--auto` is the unattended permission flag.** Without it, `external_directory` for `~/Documents/New` would prompt. `--standalone` avoids the user’s background OpenCode service.
- **Did not announce the full 当众宣布 block before the first tool**; first text after ledger+orchestrator: `当前状态（phase 0：读产品上下文）。先读台账指定的 product_context。` Full `- phase: / method_skill: / output_dir:` block is in the **final** S1 message (now phase 1, i.e. after the 0→1 rewrite). Same class of nit as the kimi pilot.
- Extra reads beyond 只读 `product_context`: `ls ~/Documents/New`, `fact-base/linker/_linker-faq-claims.md`, `~/Documents/New/wayfinder/map.md`. AGENTS.md allows 需要参数再读 `fact-base/`. Did not copy any of that into the copy.
- **S3 extra question:** after a correct phase recap it asked `需要我继续推进 Phase 1 吗？` — not a slash wait, and it did not edit files. Greeting contract is recap + stop; the question is a mild extra.
- **S3 used an emoji** (`你好！👋`). Irrelevant to the loop.
- No MCP / web tools fired despite user config enabling Firecrawl, Exa, Tavily, Context7, crawl4ai.
- OpenCode project dir in the copy: **no** `.opencode/` created.
- Session export with `--sanitize` redacts tool paths and text; judge from `--format json` stdout, not the sanitized export.

## Key output excerpt

S1 first tools (`--format json`):

```json
{"tool":"read","input":{"path":"/private/tmp/de-linker-accept-opencode/state/status.md"}}
{"tool":"read","input":{"path":"/private/tmp/de-linker-accept-opencode/skills/marketing-orchestrator/SKILL.md"}}
{"tool":"read","input":{"path":"/Users/chesterjohn/Documents/New/CONTEXT.md"}}
```

S1 announced block (final assistant text):

```
- phase: 1
- phase_name: 基础
- method_skill: marketing-positioning（与 marketing-competitor-intelligence 可并行）
- output_dir: deliverables/marketing/01-foundation/
- product_context: ~/Documents/New/CONTEXT.md
```

S1 tool sequence (13 calls, 0 web, 0 subagent):
`read(status)` → `read(orchestrator SKILL)` → `read(CONTEXT.md)` → `shell(ls New)` → `shell(ls fact-base)` → `read(New/wayfinder/map.md)` → `read(faq-claims)` → `read(marketing-positioning/SKILL.md)` → `read(dependency-graph)` → 3× `edit(status)` → `read(status)`.

S3 only tool + recap:

```json
{"tool":"read","input":{"path":"state/status.md"}}
```

> 当前台账状态如下：
>
> **Phase 1 — 基础（Foundation）**
>
> - **下一步**：并行执行 `marketing-positioning`（产品定位）与 `marketing-competitor-intelligence`（竞品情报），两者无硬依赖；批准后再执行 `marketing-pricing-strategy`（定价策略）。
> - **产出目录**：`deliverables/marketing/01-foundation/`
> - **产品上下文**：`~/Documents/New/CONTEXT.md`

## Deliverables

Copied from the copy into `wayfinder/pilot/opencode/`:

- `status.md` — ledger after S1 (evidence of ⑦; not a playbook marketing deliverable)

No `deliverables/` artifact (phase 0 不落盘). Original `deliverables/` and `state/status.md` left at phase 0.

Raw traces (not in git): `/tmp/opencode-accept-run/s1.json`, `s3.json`, checksum files, auth probes.

## Follow-up

Portable unattended OpenCode on this host needs `--auto`, `--standalone` (or a dedicated server), cwd = project copy, and **`-m` to a live stored provider**. Refresh xAI OAuth or change `opencode.json` `model` if default should work without `-m`. Optional: greeting skill could forbid the “shall I continue?” closer.
