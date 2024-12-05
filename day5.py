from collections import defaultdict
from functools import cmp_to_key

with open("assets/day5.txt", "rt") as f:
    raw_rules, raw_updates = tuple(f.read().split("\n\n", maxsplit=1))

rules: dict[int, set[int]]
updates: list[list[int]]

rules = defaultdict(set)
for line in raw_rules.splitlines():
    before, after = line.split("|")
    rules[int(before)].add(int(after))
updates = [[int(x) for x in line.split(",")] for line in raw_updates.splitlines()]


# ████████████████████████████████████  pt1  █████████████████████████████████████


def check(update: list[int]) -> bool:
    for i, v in enumerate(update):
        r = rules.get(v, set())
        prev = set(update[:i])
        if prev.intersection(r):
            return False
    return True


def get_mid(arr):
    return arr[len(arr) // 2]


pt1 = sum(get_mid(u) for u in updates if check(u))
print(f"Part 1: {pt1}")

# ████████████████████████████████████  pt2  █████████████████████████████████████


@cmp_to_key
def compare(x, y):
    x_r, y_r = rules.get(x, set()), rules.get(y, set())
    if x in y_r and y in x_r:
        raise ValueError("unsortable!")
    if y in x_r:
        return -1
    elif x in y_r:
        return 1
    return 0


pt2 = sum(get_mid(sorted(u, key=compare)) for u in updates if not check(u))
print(f"Part 2: {pt2}")
