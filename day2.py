# %%
import numpy as np

reports = []
with open("assets/day2.txt", "rt") as f:
    for line in f.read().splitlines():
        vals = [int(x) for x in line.split()]
        max_length = max(max_length, len(vals))
        reports.append(vals)


# ████████████████████████████████████  pt1  █████████████████████████████████████


def check(row: np.ndarray) -> bool:
    row_asc = np.sort(row)
    row_desc = np.flip(row_asc)
    is_sorted = (np.all(row == row_asc) or np.all(row == row_desc)).item()
    abs_diff = np.abs(row[1:] - row[:-1])
    is_diff = (abs_diff.min() >= 1) and (abs_diff.max() <= 3)
    is_safe = is_sorted and is_diff
    return is_safe


n_safe = 0
for report in reports:
    row = np.array(report)
    is_safe = check(row)
    if is_safe:
        n_safe += 1

print(f"Part 1: {n_safe}")


# ████████████████████████████████████  pt2  █████████████████████████████████████


def check_rm(row: np.ndarray) -> bool:
    for i in range(len(row)):
        rm_row = np.delete(row, i)
        if check(rm_row):
            return True
    return False


n_safe = 0
for report in reports:
    row = np.array(report)
    is_safe = check_rm(row)
    if is_safe:
        n_safe += 1

print(f"Part 2: {n_safe}")
