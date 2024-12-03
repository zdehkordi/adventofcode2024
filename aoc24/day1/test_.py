from .sol import *

DAY = 'day1'

def test_parse():
    parse(f'aoc24/{DAY}/ex.txt') == (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3]
    )

def test_gold_ex():
    assert solve(f'aoc24/{DAY}/ex.txt') == 11

def test_gold_in():
    assert solve(f'aoc24/{DAY}/in.txt') == 1873376