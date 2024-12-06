from .sol import *

DAY = 6


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == [
        [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
    ]


def test_find_carrot():
    assert find_carrot([["^"]]) == (0, 0)

    assert find_carrot(
        [
            [".", ".", "."],
            [".", ".", "."],
            [".", "^", "."],
        ]
    ) == (2, 1)


def test_no_blocks():
    assert traverse([["^"]]) == [["X"]]


def test_up_no_blocks():
    assert traverse([["."], ["."], ["^"]]) == [["X"], ["X"], ["X"]]


def test_one_block():
    assert traverse(
        [
            ["#"],
            ["."],
            ["^"],
        ]
    ) == [
        ["#"],
        ["X"],
        ["X"],
    ]


def test_one_block_turn():
    m = traverse(
        [
            ["#", "."],
            [".", "."],
            ["^", "."],
        ]
    )

    assert m == [
        ["#", "."],
        ["X", "X"],
        ["X", "."],
    ]


def test_two_block_turn():
    m = traverse(
        [
            ["#", ".", "."],
            [".", ".", "#"],
            ["^", ".", "."],
        ]
    )

    assert m == [
        ["#", ".", "."],
        ["X", "X", "#"],
        ["X", "X", "."],
    ]


def test_three_block_turn():
    m = traverse(
        [
            [".", "#", ".", "."],
            [".", ".", ".", "#"],
            [".", "^", ".", "."],
            [".", ".", "#", "."],
        ]
    )

    assert m == [
        [".", "#", ".", "."],
        [".", "X", "X", "#"],
        ["X", "X", "X", "."],
        [".", ".", "#", "."],
    ]


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 41


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 4819


def test_gold_ex2():
    assert solve2(f"aoc24/day{DAY}/ex.txt") == 6


def test_gold_in2():
    assert solve2(f"aoc24/day{DAY}/in.txt") == 1796
