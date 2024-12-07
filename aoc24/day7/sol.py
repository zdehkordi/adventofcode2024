from functools import reduce


def parse(path: str) -> list[tuple[int, list[int]]]:
    with open(path) as f:
        return [
            (
                int(line.split(":")[0]),
                list(map(int, line.split(":")[1].strip().split(" "))),
            )
            for line in f
        ]


def is_equation(val: int, nums: list[int], start: int = 0) -> bool:
    if not nums:
        return start == val
    else:
        pop = nums[0]
        return is_equation(val, nums[1:], start + pop) or is_equation(
            val, nums[1:], start * pop
        )


def solve(path: str) -> int:
    eqs = parse(path)

    return sum(eq[0] for eq in eqs if is_equation(*eq))


def is_equation2(val: int, nums: list[int], start: int = 0) -> bool:
    if not nums:
        return start == val
    else:
        pop = nums[0]
        return (
            is_equation2(val, nums[1:], start + pop)
            or is_equation2(val, nums[1:], start * pop)
            or is_equation2(val, nums[1:], int(str(start) + str(pop)))
        )


def solve2(path: str) -> int:
    eqs = parse(path)

    return sum(eq[0] for eq in eqs if is_equation2(*eq))
