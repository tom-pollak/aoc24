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

total = count_seq(views, q)

down_right = [np.diagonal(inp, k) for k in range(-n+1, n)] # down right
down_left = [np.diagonal(np.flip(inp, axis=1), k) for k in range(-n+1, n)] # left
up_right = [np.diagonal(np.flip(inp, axis=0), k) for k in range(-n+1, n)]  # up right
up_left = [np.diagonal(np.flip(inp), k) for k in range(-n+1, n)] #  up left

for row in down_right + down_left + up_right + up_left:
    total += count_seq(row, q)
print(total)

# %%
