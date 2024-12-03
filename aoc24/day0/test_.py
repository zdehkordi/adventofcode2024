from .sol import *

DAY = 0


def test_parse():
    parse(f"aoc24/day{DAY}/ex.txt") == (
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    )


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 2


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 402
