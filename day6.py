# %%
# fmt: off
import numpy as np
from jaxtyping import Int
from collections import defaultdict

blocks: set[tuple[int, int]] = set()
cur_pos: Int[np.ndarray, "2"] = None # type: ignore

direction_chars = ">v^<"

rotate_xfm = np.array(
    [[ 0, -1 ],
     [ 1,  0 ]]
)
move_xfm = np.array([0, 1]) # starts as right

def totup(arr: np.ndarray): return tuple(arr.tolist())

def rotate(move_xfm, rotate_xfm):
    return move_xfm @ rotate_xfm

with open("assets/day6.txt", "rt") as f:
    split_txt = f.read().splitlines()
    i_size, j_size = len(split_txt), None
    for i, line in enumerate(split_txt):
        if j_size is None: j_size = len(line)
        else: assert j_size == len(line)
        for j, char in enumerate(line):
            if char == ".": continue
            elif char == "#": blocks.add((i, j))
            else:
                cur_pos = np.array([i, j])
                # rotates the move_xfm to starting position
                for _ in range(direction_chars.index(char)+1):
                    move_xfm = rotate(move_xfm, rotate_xfm)

def out_of_bounds(pos, i_size, j_size):
    i, j = pos
    if i < 0 or i >= i_size or j < 0 or j >= j_size:
        return True
    return False

assert cur_pos is not None
assert totup(cur_pos) not in blocks
assert not out_of_bounds(totup(cur_pos), i_size, j_size)
assert j_size is not None

orig_move_xfm = move_xfm
orig_pos = cur_pos

# %%

move_xfm = orig_move_xfm
cur_pos = orig_pos

unique_pos: set[tuple[int, int]] = set() # type: ignore

while not out_of_bounds(cur_pos, i_size, j_size):
    unique_pos.add(totup(cur_pos))
    next_pos = cur_pos + move_xfm
    n_rotates = 0
    while totup(next_pos) in blocks:
        move_xfm = rotate(move_xfm, rotate_xfm)
        next_pos = cur_pos + move_xfm
        n_rotates += 1
        if n_rotates == 5: raise ValueError("completely spun!")
    cur_pos = next_pos

print(f"Part 1: {len(unique_pos)}")

# %%

def is_looped(cur_pos, move_xfm, blocks):
    # dict of coordingates to a set of move_xfm states we've been on this coord with
    unique_pos: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    while not out_of_bounds(cur_pos, i_size, j_size):
        if totup(move_xfm) in unique_pos[totup(cur_pos)]: return True
        unique_pos[totup(cur_pos)].add(totup(move_xfm))
        next_pos = cur_pos + move_xfm
        n_rotates = 0
        while totup(next_pos) in blocks:
            move_xfm = rotate(move_xfm, rotate_xfm)
            next_pos = cur_pos + move_xfm
            n_rotates += 1
            if n_rotates == 5: return True
        cur_pos = next_pos
    return False


total_looped = 0
for i in range(i_size):
    for j in range(j_size):
        if (i, j) == totup(orig_pos): continue
        new_blocks = blocks.copy()
        new_blocks.add((i, j))
        if is_looped(orig_pos, orig_move_xfm, new_blocks):
            print(f"{(i,j)} looped")
            total_looped += 1

print(f"Part 2: {total_looped}")
