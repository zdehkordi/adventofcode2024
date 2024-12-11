from collections import defaultdict
from typing import Generator

Cor = tuple[int, int]


def parse(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def get_frequencies(city: list[str]) -> str:
    return set("".join(city)) ^ {"."}


def get_frequency_coordinates(city: list[str]) -> dict[str, set[Cor]]:
    d = defaultdict(set)
    for f in get_frequencies(city):
        for y in range(0, len(city)):
            for x in range(0, len(city[0])):
                if city[y][x] == f:
                    d[f].add((y, x))
    return dict(d)


def get_antinode(c1: Cor, c2: Cor) -> Cor:
    return tuple(a + b for a, b in zip(c1, (c1[0] - c2[0], c1[1] - c2[1])))


def get_antinode_coordinates(city: list[str]) -> set[Cor]:
    s = set()

    ly, lx = len(city), len(city[0])

    for _, cors in get_frequency_coordinates(city).items():
        for c1 in cors:
            for c2 in [c for c in cors if c != c1]:
                y, x = get_antinode(c1, c2)
                if y >= 0 and x >= 0 and y < ly and x < lx:
                    s.add((y, x))

    return s


def solve(path: str) -> int:
    city = parse(path)
    return len(get_antinode_coordinates(city))


def get_antinodes(c1: Cor, c2: Cor) -> Generator[Cor, None, None]:
    diff = c1[0] - c2[0], c1[1] - c2[1]
    c = c1
    while True:
        node = c[0] + diff[0], c[1] + diff[1]
        yield node
        c = node


def get_antinode_coordinates2(city: list[str]) -> set[Cor]:
    s = set()

    ly, lx = len(city), len(city[0])

    for _, cors in get_frequency_coordinates(city).items():
        for c1 in cors:
            for c2 in [c for c in cors if c != c1]:
                for y, x in get_antinodes(c1, c2):
                    if y >= 0 and x >= 0 and y < ly and x < lx:
                        s.add((y, x))
                    else:
                        break
    return s


def solve2(path: str) -> int:
    city = parse(path)
    return len(get_antinode_coordinates2(city))
