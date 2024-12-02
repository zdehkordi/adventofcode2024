def parse(path: str) -> tuple[list[int], list[int]]:
    with open(path) as f:
        nums = [line.strip().split('   ') for line in f]

        return [int(x[0]) for x in nums], [int(x[1]) for x in nums]
        


def solve(path: str) -> int:
    l1, l2 = parse(path)

    return sum(abs(x - y) for x,y in zip(sorted(l1), sorted(l2)))
