#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single-line roast (1-160 characters) of the smart fridge to
/output/entry.txt. Standard library only, no network, deterministic.

The angle: not the stock "fridge orders too much milk" joke. This one
roasts a real behaviour — the fridge's internal camera plus its app
integration — and lands a double sting at the end: the appliance snitches
on your midnight snacking to your fitness app, while failing at its one
original job, keeping food fresh.
"""
import os

ROAST = "My smart fridge filmed my 2 a.m. snacking and emailed it to my fitness app \u2014 I live with a snitch that can't even keep lettuce alive."


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 160, f"roast is {len(text)} characters"
    assert "\n" not in text, "roast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
