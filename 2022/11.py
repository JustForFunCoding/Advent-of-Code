from typing import Callable
from operator import add, mul
from functools import reduce
from math import gcd
from copy import deepcopy


class Monkey:
    def __init__(
            self,
            items: list[int],
            func_str: list[str],
            div_by: int,
            idx_if_true: int,
            idx_if_false: int
            ):
        self.items = items
        self.func_str = func_str
        self.div_by = div_by
        self.idx_if_true = idx_if_true
        self.idx_if_false = idx_if_false
        self.inspected_items = 0

    def handle_turn(self, part: int) -> list[tuple[int, int]]:
        throw_away = []
        ops = {'+': add, '*': mul}
        func = lambda x: ops[self.func_str[1]](x if self.func_str[0] == 'old' else int(self.func_str[0]),
                                               x if self.func_str[2] == 'old' else int(self.func_str[2]))
        global lcm
        for item in self.items:
            item = func(item)
            if part == 1:
                item //= 3
            if part == 2:
                item %= lcm
            throw_away.append((item, self.idx_if_true) if item % self.div_by == 0 else (item, self.idx_if_false))
            self.inspected_items += 1
        self.items = []
        return throw_away


DIVS = []
lines = list(map(str.strip, open('11.in').readlines()))
MONKEYS: list[Monkey] = []
idx = idx_if_true = idx_if_false = div_by = 0
func_str: list[str]
items: list[int]
for line in lines:
    if line == '':
        MONKEYS.append(Monkey(items, func_str, div_by, idx_if_true, idx_if_false))
        continue

    words = line.strip().split(' ')
    if words[0] == 'Monkey':
        idx = int(words[1][:-1])
    elif words[0] == 'Starting':
        items = list(map(int, line.split(':')[1].strip().split(', ')))
    elif words[0] == 'Operation:':
        func_str = line.split(' = ')[1].strip().split(' ')
    elif words[0] == 'Test:':
        div_by = int(words[3])
        DIVS.append(div_by)
    elif words[1] == 'true:':
        idx_if_true = int(words[-1])
    elif words[1] == 'false:':
        idx_if_false = int(words[-1])

lcm = reduce(lambda x, y: x * y, DIVS, 1)
M = deepcopy(MONKEYS)

for part in [1,2]:
    for r in range(20 if part == 1 else 10000):
        for m in MONKEYS:
            throws = m.handle_turn(part)
            for (i, t) in throws:
                MONKEYS[t].items.append(i)

    I = sorted([m.inspected_items for m in MONKEYS], reverse=True)
    print(I[0] * I[1])
    MONKEYS = M
