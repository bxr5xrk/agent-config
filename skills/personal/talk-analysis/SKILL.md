---
name: talk-analysis
description: >-
  Turn a conference talk or video into checked, actionable changes for the
  user's own agent setup and work, not a summary. Use when the user shares a
  talk, video or AI Engineer link and asks what to apply, what it means for
  them, or to analyze it for their setup.
---

# Talk analysis

The output is a short report on the talk followed by three practical recommendations for the user's setup, checked against live files and measured on real data. The user picks which to apply; you apply them and record the choice.

## 1. Collect the material

Save everything under `/tmp/talk-analysis/<videoId>/`.

- Take talk content from MCP `ai-engineer`, not from the site HTML.
- Latest N talks: MCP records have no publish date, and the newest talks have `event: null` and empty `topics`, so MCP filters miss them. Get the order from the site catalog: read the `"release"` hash from `curl -s https://ai.engineer/talks`, then `curl -s 'https://ai.engineer/api/talks/catalog?release=<hash>'` (without `release` it returns 400). Rows of `packedCatalog.r` start with `[id, slug, title, publishedAt, durationMs, videoId, …]`; sort by `publishedAt` descending and take N. The MCP ID is `talk:<slug>`; fetch everything else from MCP.

- Transcript with timestamps. AI Engineer talks: MCP `ai-engineer` → `search` by the talk title (the MCP ID differs from the YouTube video ID), then `fetch` with `section: transcript`. If it returns `transcriptStatus: not_available`, pull YouTube captions: `uvx --from youtube-transcript-api youtube_transcript_api <videoId> --languages en --format json`, then convert the JSON (a nested list `[[{text, start, duration}]]`) to plain text with `[m:ss]` timestamps.
- The talk page article: `curl` the talk URL, parse `__NEXT_DATA__`, read `props.pageProps.model.resources.article` (sections, keyTakeaways, resources).
- The video description (chapters, links): `uvx yt-dlp --skip-download --write-description -o '/tmp/talk-analysis/<videoId>/%(id)s.%(ext)s' <url>`.
- Primary sources behind the claims. Speakers often name a library or "a paper" without a link: find them with WebSearch on the speaker's name plus the named thing, then read the repository with `gh` (README first, it shows what actually ships). If the speaker names no source and search finds none, say that the claims rest on the talk alone. When sources disagree on numbers, use the one that states the format or model version it measured, and name that version in the answer.

## 2. Extract mechanisms, not topics

Keep only "do X → get Y" mechanisms. For each:
- the mechanism in one sentence;
- evidence strength: study with numbers, demo, or speaker opinion;
- the condition under which it works.

Drop stories, customer cases and product marketing.

## 3. Read the current setup

Read the live state, not memory:
- hooks: `~/.claude/settings.json`, `~/.claude/hooks/*`, `~/Work/agent-config/hooks/` and `~/Work/agent-config/skills/work/choice-hooks/`. Not every hook has a canonical copy in `agent-config`; say where the live file is;
- rules: `~/.claude/CLAUDE.md`, `~/AGENTS.md`, `~/.cursor/rules/*.mdc`;
- skills and plugins: `~/.claude/skills` (plain folders plus symlinks into `~/Work/agent-config`, `~/.cursor/skills`, `~/.agents/skills`), `~/.claude/plugins/installed_plugins.json`. Some live hooks are hard links to their `agent-config` copy (same inode, check with `ls -i`);
- logs: `~/.claude/answer-shape.log`, session transcripts `~/.claude/projects/**/*.jsonl` (thousands of files, several GB);
- memory and recurring jobs: `~/.claude/projects/*/memory/`, `autoMemoryEnabled` in `~/.claude/settings.json`, `~/Work/agent-config/scheduled/`, `~/.codex/automations/`;
- for work-related mechanisms, the relevant repos under `~/Dev/choice` and their `.github/workflows`.

## 4. Map each mechanism

One status per mechanism, backed by a `file:line` or a command:
- already in place: where;
- partial: what is covered and what is not;
- missing;
- not applicable: one reason.

## 5. Measure the gap on real data

For partial and missing: count how often the problem the mechanism solves actually happens in the user's sessions over the last 60 days.

- Select files with `find ~/.claude/projects -name '*.jsonl' -not -path '*/subagents/*' -mtime -60`, prefilter with `grep -l` on a substring, then parse JSON lines in a Python script to pair `tool_use` with `tool_result` and count per session or per turn. `-mtime` selects files by modification time; filter messages by their `timestamp` as well.
- Prefilter substrings that also appear in system text (`git commit`, `gh pr create`) match most files; prefilter on something rarer or skip it. Judge tool success by `is_error` on the `tool_result`, not by parsing output. Split one Bash command into its separate commands before counting. `answer-shape.log` also logs drafts that were later rewritten. Forked sessions copy earlier history, so dedupe repeated items (for example by question text) before computing rates. Exclude synthetic sessions: project folders under `private-tmp` and replay or evaluation runs whose first prompt is an instruction to label, replay or review. A file write through Bash (heredoc, `tee`, `>`) counts as a write. An older study may back a number only with its date stated.
- Every number is a proxy. State what it counts and its limit in the same sentence, e.g. «у тому ж ході; інші ходи не враховано».
- If no data can measure it, say so; an unmeasured mechanism cannot get "do".

## 6. Verdict

Each action names the talk mechanism it comes from. A problem found while scanning that no mechanism of the talk addresses is not part of this answer.

Each item gets the action that closes the gap, where it goes (live file and canonical copy), rough cost, and how the user will see that it worked.

- do: the gap recurs (several cases a month or a noticeable share of sessions) and outweighs the cost of the change;
- try: a gap exists but evidence is weak, the cost is unknown, or the measurement is a loose proxy;
- not applicable: one line, including gaps too rare to pay for the change.

## Answer format

1. Report, plain text without headers: the talk's thesis in one or two sentences, then the mechanisms with their evidence (study numbers with model and format version, demo, or opinion).
2. Three recommendations as a numbered list, best first. Each says what changes, where (`file:line`), which talk mechanism it comes from, and the measured gap with its limit.
3. `AskUserQuestion` with `multiSelect: true`, one option per recommendation. The text above must be visible before the question.

## After the user chooses

Apply each chosen recommendation. For a hook edited with the Edit tool, restore its hard link to the `agent-config` copy (`cat live > canonical && ln -f canonical live`). Back up a rules file before editing it.
