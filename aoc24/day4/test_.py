from .sol import *

DAY = 4


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
    ]


def test_safe_get_2d():
    m = [
        ["M", "M", "M"],
        ["M", "S", "A"],
        ["A", "M", "X"],
    ]

    assert sg2d(m, 3, 0) == ""
    assert sg2d(m, 0, 3) == ""
    assert sg2d(m, 3, 3) == ""
    assert sg2d(m, 1, 1) == "S"
    assert sg2d(m, 2, 2) == "X"


def test_right():
    m = [
        ["X", "X", "M", "A", "S"],
    ]

    assert count_xmas(m) == 1


def test_left():
    m = [
        ["S", "A", "M", "X", "X"],
    ]

    assert count_xmas(m) == 1


def test_down():
    m = [
        ["X"],
        ["X"],
        ["M"],
        ["A"],
        ["S"],
    ]

    assert count_xmas(m) == 1


def test_up():
    m = [
        ["S"],
        ["A"],
        ["M"],
        ["X"],
        ["X"],
    ]

    assert count_xmas(m) == 1


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 18


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 2458
