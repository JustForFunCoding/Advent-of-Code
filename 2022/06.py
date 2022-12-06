from input_utils import *


def solve(n: int) -> int:
    return next((x+n for x in range(0, len(word)-n) if len(set(word[x:x+n])) == n))


word = get_lines('06.in')[0]
print(solve(4))   # part 1
print(solve(14))  # part 2
