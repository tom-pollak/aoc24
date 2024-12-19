# fmt: off
# ruff: noqa

import numpy as np

N, M = 71, 71

with open("assets/day18.txt", "rt") as f:
    lines = f.read().splitlines()
    T = len(lines)
    grid = np.zeros((T, N, M))
    blocks = [tuple(map(int, o.split(","))) for o in lines]
    for t, (j, i) in enumerate(blocks):
        grid[t:, i, j] = 1

next_post = np.array([
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
])

def find_path(grid_slice):
    visited: dict[tuple[int, int], int] = {}
    to_visit = [(0,0,0)]
    while to_visit:
        i, j, dist = to_visit.pop(0)
        for next_coords in next_post + np.array([i, j]):
            next_i, next_j = next_coords[0].item(), next_coords[1].item()
            if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:
                continue
            if grid_slice[next_i, next_j] == 1:
                continue
            if visited.get((next_i, next_j), float('inf')) > dist + 1:
                visited[(next_i, next_j)] = dist + 1
                to_visit.append((next_i, next_j, dist + 1))
    return visited.get((N-1, M-1), -1)

pt1_answer = find_path(grid[1023])
print(f"Part 1: {pt1_answer}")

def find_first_cutoff(grid):
    T, _, _ = grid.shape
    start, end = 0, T
    while start < end:
        mid = (start + end) // 2
        if find_path(grid[mid]) == -1:
            end = mid
        else:
            start = mid + 1
    return start

def find_diff(grid, t):
    idxs = np.argwhere(grid[t] - grid[t-1])
    assert idxs.shape == (1, 2)
    return idxs[0, 1].item(), idxs[0, 0].item()

cutoff_idx = find_first_cutoff(grid)
pt2_x, pt2_y = find_diff(grid, cutoff_idx)
print(f"Part 2: {pt2_x},{pt2_y}")
