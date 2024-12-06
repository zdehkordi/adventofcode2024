from itertools import cycle


def parse(path: str) -> list[list[str]]:
    with open(path) as f:
        return [[s for s in line.strip()] for line in f]


def find_carrot(matrix: list[list[str]]) -> tuple[int, int]:
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "^":
                return y, x


def traverse(matrix: list[list[str]]) -> list[list[str]]:
    y, x = find_carrot(matrix)

    ds = cycle(["u", "r", "d", "l"])
    d = next(ds)

    while y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0]):
        if d == "u":
            if matrix[y][x] == "#":
                y, x = y + 1, x + 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                y -= 1
        elif d == "r":
            if matrix[y][x] == "#":
                y, x = y + 1, x - 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                x += 1
        elif d == "d":
            if matrix[y][x] == "#":
                y, x = y - 1, x - 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                y += 1
        elif d == "l":
            if matrix[y][x] == "#":
                y, x = y - 1, x + 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                x -= 1

    return matrix


def solve(path: str) -> int:
    m = parse(path)
    m = traverse(m)
    return sum(1 for row in m for col in row if col == "X")


def is_infinite_loop(matrix: list[list[str]]) -> bool:
    y, x = find_carrot(matrix)

    seen = set()

    ds = cycle(["u", "r", "d", "l"])
    d = next(ds)

    while y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0]):
        if (y, x, d) in seen:
            return True

        if d == "u":
            if matrix[y][x] == "#":
                seen.add((y, x, d))
                y, x = y + 1, x + 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                y -= 1
        elif d == "r":
            if matrix[y][x] == "#":
                seen.add((y, x, d))
                y, x = y + 1, x - 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                x += 1
        elif d == "d":
            if matrix[y][x] == "#":
                seen.add((y, x, d))
                y, x = y - 1, x - 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                y += 1
        elif d == "l":
            if matrix[y][x] == "#":
                seen.add((y, x, d))
                y, x = y - 1, x + 1
                d = next(ds)
            else:
                matrix[y][x] = "X"
                x -= 1

    return False


def solve2(path: str) -> int:
    m = parse(path)

    y_car, x_car = find_carrot(m)

    count = 0

    for y in range(len(m)):
        for x in range(len(m[0])):
            if (y, x) != (y_car, x_car):
                sample = [r[:] for r in m]
                sample[y][x] = "#"
                count += 1 if is_infinite_loop(sample) else 0

    return count
