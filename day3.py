import re

with open("assets/day3.txt", "rt") as f:
    txt = f.read()


def get_sum(txt: str) -> int:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", txt)
    return sum(int(x) * int(y) for x, y in matches)


print(f"Part 1: {get_sum(txt)}")

post, do, total = txt, True, 0
while True:
    pattern = r"don't\(\)" if do else r"do\(\)"  # find opposite marker
    match = re.search(pattern, post)
    if match is None:
        if do:
            total += get_sum(post)
        break
    pre, post = post[: match.end()], post[match.end() :]
    if do:
        total += get_sum(pre)
    do = not do

print(f"Part 2: {total}")
