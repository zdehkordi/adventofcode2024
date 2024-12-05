from collections import defaultdict

Rules = dict[int, list[int]]
Update = list[int]
Updates = list[Update]


def parse(path: str) -> tuple[Rules, Updates]:
    with open(path) as f:
        raw_rules, updates = f.read().split("\n\n")

        rules = defaultdict(list)

        for rule in raw_rules.split("\n"):
            before, after = map(int, rule.split("|"))
            rules[before].append(after)

        return dict(rules), [
            [int(u) for u in update.split(",")] for update in updates.split("\n")
        ]


def is_valid(rules: Rules, update: list[int]) -> bool:
    seen = []
    for u in update:
        if u in rules and any(x in seen for x in rules[u]):
            return False

        seen.append(u)
    return True


def middle(update: list[int]) -> int:
    return update[len(update) // 2]


def solve(path: str) -> int:
    rules, updates = parse(path)

    return sum(map(middle, filter(lambda u: is_valid(rules, u), updates)))
