from input_utils import *


lines = list(map(lambda l: l.rstrip(), get_lines('05.in')))
crates_cnt = 9
crates: list[list[str]] = [[] for _ in range(crates_cnt)]

for line in lines:
    if '[' not in line:
        map(lambda c: c.reverse(), crates)
        break
    for s in range(0, len(line), 4):
        elem = line[s:s+4]
        if '[' in elem:
            crates[s//4].append(elem[1])

for line in lines:
    if 'move' not in line:
        continue
    words = line.split(' ')
    cnt, from_, to_ = int(words[1]), int(words[3])-1, int(words[5])-1
    to_move = crates[from_][:cnt]
    crates[from_] = crates[from_][cnt:]
    # crates[to_] = list(reversed(to_move)) + crates[to_]  # part 1
    crates[to_] = to_move + crates[to_]                  # part 2

print("".join(map(lambda c: c.pop(0), crates)))
