from collections import defaultdict
from functools import cmp_to_key

with open("assets/day5.txt", "rt") as f:
    r, updates = tuple(f.read().split("\n\n", maxsplit=1))
    rules = defaultdict(set)
    for line in r.splitlines():
        before, after = line.split("|")
        rules[int(before)].add(int(after))
    rules = dict(rules)
    updates = [
        [int(x) for x in line.split(",")] for line in updates.splitlines() if line
    ]


# ████████████████████████████████████  pt1  █████████████████████████████████████


def check(update: list[int]) -> bool:
    for i, v in enumerate(update):
        r = rules.get(v, set())
        prev = set(update[:i])
        if prev.intersection(r):
            return False
    return True


total = 0
for update in updates:
    if check(update):
        mid = update[len(update) // 2]
        total += mid

print(f"Part 1: {total}")

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


total = 0
for update in updates:
    if not check(update):
        update.sort(key=compare)
        mid = update[len(update) // 2]
        total += mid

print(f"Part 2: {total}")
