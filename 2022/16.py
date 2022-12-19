from input_utils import get_lines
from collections import defaultdict


def solve(valve: str, t: int, pressure: int, opened: int) -> int:
    idx = INDEX_OF[valve]

    if (idx, t, pressure, opened) in MEMO:
        return MEMO[(idx, t, pressure, opened)]

    if t == 0:
        res = pressure
    else:
        res = 0
        # Try to open this valve (if not alr opened)
        if opened & (1 << idx) == 0 and P[valve] > 0:
            res = max(res,
                      solve(valve, t - 1,
                            pressure + P[valve] * (t - 1),
                            opened | (1 << idx)))

        # Try to move to some neighbor
        for neigh in ADJ[valve]:
            res = max(res, solve(neigh, t - 1, pressure, opened))

    MEMO[(idx, t, pressure, opened)] = res
    return MEMO[(idx, t, pressure, opened)]


lines = get_lines('16.in')
ADJ = defaultdict(list)
P = {}
INDEX_OF: dict[str, int] = {}
for line in lines:
    words = line.split(' ')
    P[words[1]] = int(words[4].split('=')[1][:-1])
    neighs = ''.join(words[9:]).split(',')
    for neigh in neighs:
        ADJ[words[1]].append(neigh)
    INDEX_OF[words[1]] = len(INDEX_OF)

MEMO: dict[tuple[int, int, int, int], int] = {}
print(solve('AA', 30, 0, 0))
