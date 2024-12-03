from .sol import *

DAY = 3


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == [
        (2, 4),
        (5, 5),
        (11, 8),
        (8, 5),
    ]


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 161


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 178886550
