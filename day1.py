import numpy as np

with open("assets/day1_p1.txt", "rt") as f:
    inp = np.array([[int(x) for x in line.split()] for line in f.read().splitlines()])

l, r = inp[:, 0], inp[:, 1]
pt1_answer = np.abs(np.sort(l) - np.sort(r)).sum().item()
print(f"Part 1: {pt1_answer}")

shared_mask = np.isin(r, l)
r_vals, r_counts = np.unique(r[shared_mask], return_counts=True)
pt2_answer = np.sum(r_vals * r_counts).item()
print(f"Part 2: {pt2_answer}")
