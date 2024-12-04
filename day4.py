# %%
# fmt: off
import numpy as np
from jaxtyping import Float, Int, jaxtyped
from beartype import beartype as typechecker



np.set_printoptions(linewidth=200)
s2i = {s: i for i, s in enumerate("XMAS")}

with open("assets/day4_b.txt", "r") as f:
    inp = np.array([[s2i[c] for c in line] for line in f.read().splitlines()])

q = np.arange(4)
n, m = inp.shape

# %%

@jaxtyped(typechecker=typechecker)
def count_seq(arr: Int[np.ndarray, "*n m"], pattern: Int[np.ndarray, "d"]) -> int:
    "works with both 1D and 2D arrays"
    if arr.shape[-1] < len(pattern):
        return 0
    windows: Float[np.ndarray, "*n m-d+1 d"] = np.lib.stride_tricks.sliding_window_view(arr, len(pattern), axis=-1)
    return np.sum(np.all(windows == pattern, axis=-1)).item()

# %%
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

# %%
