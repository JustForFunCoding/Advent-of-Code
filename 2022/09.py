from input_utils import *
from collections import defaultdict


def corrigate(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail
    dx, dy = abs(hx - tx), abs(hy - ty)

    if dx <= 1 and dy <= 1:
        return tail
    return ((hx + tx) // 2 if dx >= 2 else hx, (hy + ty) // 2 if dy >= 2 else hy)


lines = get_lines('09.in')
head = (0, 0)
tails = [(0, 0) for _ in range(9)]
DX = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
DY = {'R': 0, 'L': 0, 'U': -1, 'D': 1}
P1: set[tuple[int, int]] = {tails[0]}
P2: set[tuple[int, int]] = {tails[-1]}

for cmd in lines:
    words = cmd.split(' ')
    direction, length = words[0], int(words[1])

    for _ in range(length):
        head = (head[0] + DX[direction], head[1] + DY[direction])
        tails[0] = corrigate(head, tails[0])
        for i in range(1, 9):
            tails[i] = corrigate(tails[i-1], tails[i])
        P1.add(tails[0])
        P2.add(tails[-1])

print(len(P1))
print(len(P2))
