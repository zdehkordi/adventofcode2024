from pathlib import Path

from .sol import *


DAY = Path(__file__).parent.name.split("day")[1]


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == ()


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 2


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 402
