from copy import deepcopy
from functools import reduce
import math


M = []
OP = []
DIV = []
TRUE = []
FALSE = []
for group in open('11.in').read().split('\n\n'):
    if group == '':
        continue
    id_, items, op, test, true, false = group.split('\n')
    M.append(list(map(int, items.split(': ')[1].strip().split(', '))))
    OP.append(eval('lambda old: ' + op.split(' = ')[1]))
    DIV.append(int(test.split(' ')[-1]))
    TRUE.append(int(true.split(' ')[-1]))
    FALSE.append(int(false.split(' ')[-1]))

cm = reduce(lambda x, y: x * y, DIV, 1)
gcd = reduce(lambda x, y: math.gcd(x, y), DIV, 0)
lcm = cm // gcd
M_ORIG = deepcopy(M)

for part in [1, 2]:
    C = [0 for _ in range(len(M))]
    for r in range(20 if part == 1 else 10_000):
        for i in range(len(M)):
            for item in M[i]:
                item = OP[i](item)
                if part == 1:
                    item //= 3
                if part == 2:
                    item %= lcm
                M[TRUE[i] if item % DIV[i] == 0 else FALSE[i]].append(item)
            C[i] += len(M[i])
            M[i] = []

    M = deepcopy(M_ORIG)
    C = sorted(C, reverse=True)
    print(C[0] * C[1])
