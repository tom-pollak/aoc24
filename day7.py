# fmt: off
# ruff: noqa
data = []
with open("assets/day7.txt", "rt") as f:
    for line in f.read().splitlines():
        answer, inps = tuple(line.split(":"))
        answer = int(answer)
        inps = [int(x) for x in inps.split()]
        data.append((inps, answer))

def calc(x, y, op) -> int:
    match op:
        case "+": return x + y
        case "*": return x * y
        case "|": return int(str(x) + str(y))
        case _: raise ValueError(f"undefined op: {op}")

def can_be_solved(inps: list[int], answer: int, curr_sum: int, ops: str) -> bool:
    if not inps: return curr_sum == answer
    next_v, rest = inps[0], inps[1:]
    for op in ops:
        if can_be_solved(rest, answer, curr_sum=calc(curr_sum, next_v, op), ops=ops):
            return True
    return False

def solve_all(data, ops):
    return sum(answer for inps, answer in data
               if can_be_solved(inps[1:], answer, curr_sum=inps[0], ops=ops))

print(f"Part 1: {solve_all(data, ops="+*")}")
print(f"Part 2: {solve_all(data, ops="+*|")}")
