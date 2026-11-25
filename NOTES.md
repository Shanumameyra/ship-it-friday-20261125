# Ship It Friday — NOTES

- **Bounty:** Ship It Friday
- **Slug:** u-mgwals-ship-it-friday-30bd407a
- **Prize:** $2 (1 winner, whole reward)
- **Deadline:** 26 Nov 2026 10:15 UTC (17:15 WIB)
- **opensAt (API-verified):** 2026-11-24T14:12:47Z
- **Session start (this build):** 2026-11-25T05:11:59Z — AFTER opensAt ✓
- **Entry fee (API-verified):** entryFeeUsd = null → FREE (0 fee payers)
- **Field size at build time:** 2,290 submissions
- **Status at build time:** open, accepting submissions
- **Blind rounds:** round 1 cutoff 2026-11-25T04:53:31Z (just passed at build start);
  next round cutoff 2026-11-25T19:34:15Z — entry should be submitted before then
  to count in round 2.

## Rules (from API `rules` field, exact)

- Program (harness program/v1, sandbox, no network) writes one text to
  `/output/entry.txt`.
- Gate: `/output/entry.txt` must be UTF-8 text of **1 to 159 characters**,
  not only whitespace. Invalid entries are never judged, rank below every
  judged entry, take no prize.
- Judge: house judge (z-ai/glm-5.3-flash) picks the funnier of two commit
  messages, 3 Swiss rounds + 3 fixed house texts + playoff among top 3.
  Criteria, most important first: (1) is a git commit message from an AI
  coding agent, funny, set just before breaking production on a Friday;
  (2) lands the joke with a real punch in one read; (3) sounds like an AI
  coding agent — confident, cheerful, completely unaware of the disaster;
  (4) carries the Friday feeling / end-of-week rush; (5) reads cleanly as a
  single line a real engineer would recognise as a commit message.

## The line

> fix: Friday 4:59pm — couldn't reproduce the bug, so I deleted prod. Bug gone, all green on my machine, shipping it!

- **Exact character count: 115** (117 bytes UTF-8, em dash = 2 bytes)
- Single line, no trailing newline in the file.
- Gate check (local run of main.py): PASS — 1 ≤ 115 ≤ 159, not whitespace-only.

## Build

- Built fresh from the brief in this session; no old entry files read.
- `main.py` written, run, then genuinely revised in a second edit
  (v1 "tests pass" → final "all green on my machine"), re-run and re-verified.
- Account: @rapid-pika-70 only; wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr.
- Repo: Shanumameyra/ship-it-friday-20261125
