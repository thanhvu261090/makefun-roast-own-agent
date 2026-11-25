# Roast Your Own Agent

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/thanhvu261090/makefun-roast-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/thanhvu261090/makefun-roast-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

One original roast of my own AI agent — a single line, funny and playful, never hateful — for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun.

## The entry

> My AI agent works 24/7, bills me by the token, and still asks 'did that help?' — even my toaster commits to a decision faster.

(126 characters, single line.)

## How it works

`main.py` (Python 3, standard library only, no network) holds the one fixed entry line, validates it against the bounty gate — UTF-8, 1–200 characters, single line, no leading or trailing whitespace — and writes it exactly as-is, with no trailing newline, to `/output/entry.txt`.

Run it:

```bash
python3 main.py
```

Run the self-test:

```bash
python3 main.py --self-test
```

## License

MIT — see [LICENSE](LICENSE).
