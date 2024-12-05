from .sol import *

DAY = 5


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == (
        {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        },
        [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ],
    )


def test_simple_valid():
    assert is_valid({11: [22], 22: [33]}, [11, 22, 33])


def test_simple_not_valid():
    assert not is_valid({22: [11]}, [11, 22, 33])


def test_middle():
    assert middle([61, 13, 29]) == 13
    assert middle([97, 13, 75, 29, 47]) == 75


def test_fix():
    assert fix({29: [13], 61: [29]}, [61, 13, 29]) == [61, 29, 13]


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 143


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 5452


def test_gold_ex_2():
    assert solve2(f"aoc24/day{DAY}/ex.txt") == 123


def test_gold_in_2():
    assert solve2(f"aoc24/day{DAY}/in.txt") == 4598
