# fmt: off
import numpy as np
import torch as t
import torch.nn.functional as F
from jaxtyping import Float, Int, jaxtyped
from beartype import beartype as typechecker

# ████████████████████████████████████  pt1  █████████████████████████████████████

s2i = {s: i for i, s in enumerate("XMAS")}

with open("assets/day4_b.txt", "r") as f:
    inp = np.array([[s2i[c] for c in line] for line in f.read().splitlines()])

q = np.arange(4)
n, m = inp.shape

@jaxtyped(typechecker=typechecker)
def count_seq(arr: Int[np.ndarray, "*n m"], pattern: Int[np.ndarray, "d"]) -> int:
    "works with both 1D and 2D arrays"
    if arr.shape[-1] < len(pattern):
        return 0
    windows: Float[np.ndarray, "*n m-d+1 d"] = np.lib.stride_tricks.sliding_window_view(arr, len(pattern), axis=-1)
    return np.sum(np.all(windows == pattern, axis=-1)).item()

views = np.concatenate([
    inp, # right
    np.flip(inp, axis=1), # left
    inp.T, # down
    np.flip(inp.T, axis=1) # up
])

pt1_answ = count_seq(views, q)

diagonals = []
for v_flip in False, True:
    for h_flip in False, True:
        arr = np.flip(inp, 0) if v_flip else inp
        arr = np.flip(arr, 1) if h_flip else arr
        diagonals.extend([np.diagonal(arr, k) for k in range(-n+1, n)])

for row in diagonals:
    pt1_answ += count_seq(row, q)
print(f"Part 1: {pt1_answ}")

# ████████████████████████████████████  pt2  █████████████████████████████████████

s2oh = {s: np.eye(4)[i] for i, s in enumerate("XMAS")}

with open("assets/day4_b.txt", "r") as f:
    inp = t.tensor([[s2oh[c] for c in line] for line in f.read().splitlines()], dtype=t.float32)


Z = t.zeros(4).tolist() # blank space
_, M, A, S = tuple(s2oh.values())

# our kernel!
k = t.tensor([
    [M, Z, S],
    [Z, A, Z],
    [M, Z, S],
], dtype=t.float32)

sum_to_find = k.sum()

views = t.stack([
    k,
    k.flip(1),
    t.rot90(k, 1, [0,1]),
    t.rot90(k, -1, [0,1]),
])

output = F.conv2d(input=inp.permute(2, 0, 1)[None], weight=views.permute(0, 3, 1, 2))
pt2_answ = t.sum(output == sum_to_find).item()
print(f"Part 2: {pt2_answ}")
