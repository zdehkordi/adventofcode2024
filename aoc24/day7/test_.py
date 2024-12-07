from .sol import *

DAY = 7


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]


def test_add_true():
    assert is_equation(6, [1, 2, 3])


def test_add_false():
    assert not is_equation(5, [1, 2, 6])


def test_mul_true():
    assert is_equation(1, [1, 1, 1])


def test_mul_false():
    assert not is_equation(1, [1, 1, 2])


def test_add_and_mul():
    assert is_equation(20, [1, 3, 5])


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 3749


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 1708857123053


def test_gold_ex2():
    assert solve2(f"aoc24/day{DAY}/ex.txt") == 11387


def test_gold_in2():
    assert solve2(f"aoc24/day{DAY}/in.txt") == 189207836795655
