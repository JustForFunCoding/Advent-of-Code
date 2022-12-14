from input_utils import *
from collections import deque


lines = get_lines('12.in')
G = []
for line in lines:
    G.append(list(line))
R, C = len(G), len(G[0])

E_r = E_c = -1
S_r = S_c = -1
STARTS = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            G[r][c] = 'a'
            S_r, S_c = r, c
        elif G[r][c] == 'E':
            E_r, E_c = r, c
            G[r][c] = 'z'
        if G[r][c] == 'a':
            STARTS.append((r, c))


def bfs(starts: list[tuple[int, int]], part: int) -> int:
    DIFFS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    best = 100_000

    Q: deque[tuple[int, int, int]] = deque([])
    for (r, c) in starts:
        Q.append((r, c, 0))
    VIS = set()

    while Q:
        r, c, dist = Q.popleft()
        if (r, c) in VIS:
            continue
        VIS.add((r, c))
        if (r, c) == (E_r, E_c):
            return dist
        for (dr, dc) in DIFFS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and ord(G[rr][cc]) <= ord(G[r][c]) + 1:
                Q.append((rr, cc, dist + 1))

    return best


print(bfs([(S_r, S_c)], 1))
print(bfs(STARTS, 2))
