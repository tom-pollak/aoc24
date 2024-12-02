import numpy as np

# Shame it's disjoint, otherwise this could be one big ol' matrix
with open("assets/day2.txt", "rt") as f:
    reports = [
        np.array([int(x) for x in line.split()]) for line in f.read().splitlines()
    ]


# ████████████████████████████████████  pt1  █████████████████████████████████████


def check(report: np.ndarray) -> bool:
    report_asc = np.sort(report)
    report_desc = np.flip(report_asc)
    is_sorted = (np.all(report == report_asc) or np.all(report == report_desc)).item()
    abs_diff = np.abs(report[1:] - report[:-1])
    is_diff = (abs_diff.min() >= 1) and (abs_diff.max() <= 3)
    is_safe = is_sorted and is_diff
    return bool(is_safe)


n_safe = sum(check(report) for report in reports)
print(f"Part 1: {n_safe}")


# ████████████████████████████████████  pt2  █████████████████████████████████████


def check_rm(row: np.ndarray) -> bool:
    for i in range(len(row)):
        rm_row = np.delete(row, i)
        if check(rm_row):
            return True
    return False


n_safe = sum(check_rm(report) for report in reports)
print(f"Part 2: {n_safe}")
