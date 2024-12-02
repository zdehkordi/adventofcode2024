from .day1 import *

def test_parse():
    parse('aoc24/day1/ex.txt') == (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3]
    )

def test_gold_ex():
    assert solve('aoc24/day1/ex.txt') == 11

def test_gold_in():
    assert solve('aoc24/day1/in.txt') == 1873376