# Review Journal

The repository goal stays the same: package a Python local lab for pack analysis with round-trip fixtures, lossless normalization checks, and documented operating limits. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 152, lane `ship`
- `stress`: `terminal width`, score 184, lane `ship`
- `edge`: `argument risk`, score 176, lane `ship`
- `recovery`: `report density`, score 125, lane `watch`
- `stale`: `file span`, score 207, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
