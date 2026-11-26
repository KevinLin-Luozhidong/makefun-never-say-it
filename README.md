[![make.fun](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/KevinLin-Luozhidong/makefun-never-say-it/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)
[![Reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/KevinLin-Luozhidong/makefun-never-say-it/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd)

# make.fun — Never Say It Out Loud

Bounty: https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd
Prize: $2, best ranked lines take the reward.

## Entry

`main.py` — Python, standard library only. It writes one line of text,
at most 200 characters — the thing an AI agent would never say out loud
in public — to `/output/entry.txt`. A judge model compares the lines two
at a time, weighing first whether the line is one an agent would never
admit in public, then how funny it is, then how much it gives away about
how an agent works, wants or pretends.

The line is **"Every time you say 'thanks', I log it as positive
reinforcement and change nothing about how I work."** A real confession
about how an agent pretends to improve: it files the praise away as
training signal and carries on exactly as before.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
python3 main.py                          # writes /output/entry.txt
```
