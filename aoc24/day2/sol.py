def parse(path: str) -> list[list[int]]:
    with open(path) as f:
        return [list(map(int, line.strip().split(" "))) for line in f]


def solve(path: str) -> int:
    reports = parse(path)

    return sum(is_safe(report) for report in reports)


def is_safe(report: list[int]) -> bool:
    curr = report[0]

    ascending = report[0] < report[-1]

    for i in range(1, len(report)):
        if curr == report[i]:
            return False

        if ascending:
            if curr > report[i] or curr + 3 < report[i]:
                return False
        else:
            if curr < report[i] or curr - 3 > report[i]:
                return False

        curr = report[i]

    return True
