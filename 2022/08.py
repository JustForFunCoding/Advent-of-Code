from input_utils import *
from functools import reduce


def is_visible(r: int, c: int) -> bool:
    return reduce(max, G[r][:c], -1) < G[r][c] or \
        reduce(max, G[r][c+1:], -1) < G[r][c] or \
        reduce(max, [G[rr][c] for rr in range(r)], -1) < G[r][c] or \
        reduce(max, [G[rr][c] for rr in range(r+1, R)], -1) < G[r][c]


def scenic_score(r: int, c: int) -> int:
    DIFF = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    score = 1
    for (dr, dc) in DIFF:
        rr, cc = r + dr, c + dc
        while True:
            if not (0 <= rr < R and 0 <= cc < C):
                rr -= dr
                cc -= dc
                break
            if G[rr][cc] >= G[r][c]:
                break
            rr += dr
            cc += dc
        score *= abs((rr - r) + (cc - c)) if rr != r or cc != c else 1
    return score


lines = get_lines('08.in')
G = []
for line in lines:
    G.append(list(map(int, list(line))))

R, C = len(G), len(G[0])
p1 = 2 * (R + C) - 4
p2 = 1
for r in range(1, R - 1):
    for c in range(1, C - 1):
        if is_visible(r, c):
            p1 += 1
        p2 = max(p2, scenic_score(r, c))

print(p1)
print(p2)
