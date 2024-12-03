from .sol import *

DAY = 0


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == ()


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 2


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 402
