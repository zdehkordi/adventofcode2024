from typing import Iterable


def parse(path: str) -> list[list[str]]:
    with open(path) as f:
        return [[c for c in line.strip()] for line in f]


def sg2d(m: list[list], y: int, x: int):
    """short for safe get 2d"""
    return m[y][x] if 0 <= y < len(m) and 0 <= x < len(m[0]) else ""


def check(s_iter: Iterable[str]) -> int:
    s = "".join(s_iter)
    return 1 if s == "MAS" else 0


def count_xmas(m: list[list[str]]) -> int:
    count = 0

    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "X":
                count += check(sg2d(m, y, x + i) for i in range(1, 4))
                count += check(sg2d(m, y, x - i) for i in range(1, 4))
                count += check(sg2d(m, y + i, x) for i in range(1, 4))
                count += check(sg2d(m, y - i, x) for i in range(1, 4))

                count += check(sg2d(m, y + i, x + i) for i in range(1, 4))
                count += check(sg2d(m, y + i, x - i) for i in range(1, 4))
                count += check(sg2d(m, y - i, x + i) for i in range(1, 4))
                count += check(sg2d(m, y - i, x - i) for i in range(1, 4))

    return count


def solve(path: str) -> int:
    m = parse(path)

    return count_xmas(m)
