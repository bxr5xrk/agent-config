# Decisions on past recommendations

Read before proposing actions. Do not propose a declined action again unless new data changes the case; if it does, say what changed.

## Accepted

- 2026-11-08, "Make Your AI Agents Predictable With Graph Engineering": removed the self-confidence rule «If anything is uncertain… ask Vasyl first» from `~/AGENTS.md`; concrete triggers stay in `~/.claude/CLAUDE.md` «Asking vs proceeding».
- 2026-11-08, same talk: banned phrases from `answer-shape-log.py` now force a rewrite in `answer-review.py`, also for short replies, without an extra model call.
- 2026-11-08, same talk: split AskUserQuestion history by question type. Result: the recommended option was taken in 53% of 1382 unique questions over 60 days, no generic type above 70% (tests, git, migration). No «proceed» rule was added.

## Declined

- 2026-11-08: a Stop or push hook that blocks «готово» or `git push` until jest/eslint ran after the last JS edit.
- 2026-11-08: a hook that gates writes to the production Mongo database.
