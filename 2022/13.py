from input_utils import get_lines, get_line_groups
from functools import cmp_to_key


def compare(p1: int | list[int], p2: int | list[int]) -> int:
    if isinstance(p1, list) and isinstance(p2, list):
        if p1 == [] and p2 != []:
            return -1
        elif p1 != [] and p2 == []:
            return 1
        elif p1 == p2 == []:
            return 0
        h1, h2 = p1[0], p2[0]
        res = compare(h1, h2)
        return res if res != 0 else compare(p1[1:], p2[1:])
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)
    elif isinstance(p1, list) and isinstance(p2, int):
        return compare(p1, [p2])
    else:
        assert isinstance(p1, int) and isinstance(p2, int)
        return -1 if p1 < p2 else 0 if p1 == p2 else 1


GROUPS = get_line_groups('13.in')
total = 0
for i, group in enumerate(get_line_groups('13.in')):
    p1, p2 = group
    if compare(eval(p1), eval(p2)) == -1:
        total += i + 1
print(total)  # part 1


PACKETS = list(map(eval, filter(lambda l: l != '', get_lines('13.in'))))
if PACKETS.count([[2]]) == 0:
    PACKETS.append([[2]])
if PACKETS.count([[6]]) == 0:
    PACKETS.append([[6]])
PACKETS = sorted(PACKETS, key=cmp_to_key(compare))
i2 = PACKETS.index([[2]]) + 1
i6 = PACKETS.index([[6]]) + 1
print(i2 * i6)  # part 2
