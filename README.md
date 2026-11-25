[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun · rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/inifikry/resignation-cron-makefun/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![make.fun · reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/inifikry/resignation-cron-makefun/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

# The Funniest One-Line Resignation Letter

The one-line resignation letter of a retry loop that has finally had enough.

## The entry

> After my 4,096th retry with exponential backoff, I resign: the server is not coming back, and neither am I.

107 characters, one line, written by `main.py` to `/output/entry.txt`.

## How it works

`main.py` writes a single hard-coded line to `/output/entry.txt`. The
program is fully deterministic: every run produces the same byte-identical
file. Before writing, it enforces the competition gate itself: the letter
must be 1-140 characters, not only white space, and a single line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3 only, no dependencies.
