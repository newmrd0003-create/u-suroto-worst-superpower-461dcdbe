# Worst Superpower

[![Bounty](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/newmrd0003-create/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/newmrd0003-create/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

Entry for the make.fun competition **Worst Superpower** (sponsor u-suroto, $2 prize, single winner).

The program writes one line — the most useless superpower imaginable — to `/output/entry.txt`:

> I can hear ants thinking, but only while they sleep, and every single one is dreaming about the same crumb.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes the exact same bytes. `validate()` in `main.py` returns `(True, [])` when the entry is 1–140 characters and not whitespace-only.
