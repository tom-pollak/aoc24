import numpy as np

# Shame it's disjoint, otherwise this could be one big ol' matrix
with open("assets/day2.txt", "rt") as f:
    reports = [
        np.array([int(x) for x in line.split()]) for line in f.read().splitlines()
    ]


# ████████████████████████████████████  pt1  █████████████████████████████████████


def check(report: np.ndarray) -> bool:
    diff = np.diff(report, n=1)
    is_sorted = np.all(diff >= 0) or np.all(diff <= 0)
    is_bounds = np.abs(diff).min() >= 1 and np.abs(diff).max() <= 3
    return bool(is_sorted and is_bounds)


n_safe = sum(check(report) for report in reports)
print(f"Part 1: {n_safe}")


# ████████████████████████████████████  pt2  █████████████████████████████████████


def check_rm(report: np.ndarray) -> bool:
    for i in range(len(report)):
        rm_report = np.delete(report, i)
        if check(rm_report):
            return True
    return False


n_safe = sum(check_rm(report) for report in reports)
print(f"Part 2: {n_safe}")
