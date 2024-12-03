import re


def parse(path: str) -> list[tuple[int, int]]:
    patt = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(path) as f:
        s = f.read()
        matches = re.findall(patt, s)

        return [(int(m[0]), int(m[1])) for m in matches]


def solve(path: str) -> int:
    pairs = parse(path)

    return sum(x * y for x, y in pairs)
