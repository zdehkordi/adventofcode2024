from .sol import *

DAY = "day2"


def test_parse():
    parse(f"aoc24/{DAY}/ex.txt") == (
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    )


def test_safe_ascending():
    assert is_safe([1, 2, 3])


def test_safe_ascending():
    assert is_safe([3, 2, 1])


def test_not_safe_ascend_then_descend():
    assert not is_safe([1, 2, 1])


def test_not_safe_descend_then_ascend():
    assert not is_safe([2, 1, 2])


def test_not_safe_big_ascend():
    assert not is_safe([1, 2, 6])


def test_not_safe_big_descend():
    assert not is_safe([6, 2, 1])


def test_not_safe_flat():
    assert not is_safe([1, 1, 1])


def test_gold_ex():
    assert solve(f"aoc24/{DAY}/ex.txt") == 2


def test_gold_in():
    assert solve(f"aoc24/{DAY}/in.txt") == 402
