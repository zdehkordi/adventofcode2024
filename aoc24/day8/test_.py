from .sol import *

DAY = 8


def test_parse():
    assert parse(f"aoc24/day{DAY}/ex.txt") == [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]


def test_get_frequencies():
    assert get_frequencies(["A..c", "8..D"]) == {"A", "8", "c", "D"}


def test_get_frequency_coordinates():
    assert get_frequency_coordinates(["A..c", "8..D"]) == {
        "A": {(0, 0)},
        "8": {(1, 0)},
        "c": {(0, 3)},
        "D": {(1, 3)},
    }


def test_get_antinode():
    assert get_antinode((1, 1), (2, 2)) == (0, 0)
    assert get_antinode((2, 2), (1, 1)) == (3, 3)


def test_get_antinodes():
    antinodes = get_antinodes((2, 2), (1, 1))
    assert next(antinodes) == (3, 3)
    assert next(antinodes) == (4, 4)
    assert next(antinodes) == (5, 5)


def test_get_antinodes_square():
    antinodes = get_antinodes((2, 2), (1, 0))
    assert next(antinodes) == (3, 4)
    assert next(antinodes) == (4, 6)
    assert next(antinodes) == (5, 8)


def test_antinode():
    assert get_antinode_coordinates(
        [
            "....",
            ".0..",
            "..0.",
            "....",
        ]
    ) == {(0, 0), (3, 3)}


def test_antinode_out_of_bounds():
    assert (
        len(
            get_antinode_coordinates(
                [
                    ".0..",
                    "..0.",
                ]
            )
        )
        == 0
    )


def test_gold_ex():
    assert solve(f"aoc24/day{DAY}/ex.txt") == 14


def test_gold_in():
    assert solve(f"aoc24/day{DAY}/in.txt") == 295


def test_gold_ex2():
    assert solve2(f"aoc24/day{DAY}/ex.txt") == 34


def test_gold_in2():
    assert solve2(f"aoc24/day{DAY}/in.txt") == 402
