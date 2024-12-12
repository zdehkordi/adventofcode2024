from .sol import *

DAY = 9


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == list(
        "00...111...2...333.44.5555.6666.777.888899"
    )


def test_swap():
    assert swap(list("00...111...2...333.44.5555.6666.777.888899")) == list(
        "0099811188827773336446555566.............."
    )


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 1928


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 6279058075753
