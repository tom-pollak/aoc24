# fmt: off
# ruff: noqa

from functools import cache

with open("assets/day19.txt", "rt") as f:
    lines = f.read().splitlines()
    combos = set(lines.pop(0).split(", "))
    assert lines[0] == ""
    patterns = lines[1:]

def match_pt1(pattern):
    if len(pattern) == 0: return True
    for i in range(1, len(pattern)+1):
        if pattern[:i] in combos and match_pt1(pattern[i:]):
            return True
    return False

pt1_answer = sum(int(match_pt1(pattern)) for pattern in patterns)
print(f"Part 1: {pt1_answer}")

@cache
def match_pt2(pattern):
    if len(pattern) == 0: return 1
    total = 0
    for i in range(1, len(pattern)+1):
        if pattern[:i] in combos:
            total += match_pt2(pattern[i:])
    return total


pt2_answer = sum(int(match_pt2(pattern)) for pattern in patterns)
print(f"Part 2: {pt2_answer}")
