from input_utils import *


def priority(c: str) -> int:
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 26 + 1


lines = get_lines('03.in')
p1 = sum(map(lambda s: priority((set(s[:len(s)//2]) & set(s[len(s)//2:])).pop()), lines))
groups = [ list(map(lambda s: s.strip(), lines[i:i+3])) for i in range(0, len(lines), 3) ]
p2 = sum(map(lambda g: priority((set(g[0]) & set(g[1]) & set(g[2])).pop()), groups))

print(p1)
print(p2)
