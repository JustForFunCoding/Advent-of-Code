from input_utils import *
from collections import defaultdict


lines = get_lines('07.in')


dir_stack: list[str] = []
dirs: dict[str, int] = defaultdict(int)
for cmd in lines:
    act_dir = dir_stack[-1] if len(dir_stack) > 0 else ''
    words = cmd.split(' ')
    if words[0] == '$':
        if words[1] == 'cd':
            if words[2] == '..':
                dir_stack.pop()
            else:
                dir_stack.append(words[2])
    else:
        if words[0].isnumeric():
            for i in range(len(dir_stack)):
                path = '/'.join(dir_stack[:i+1])[1:] + '/'
                dirs[path] += int(words[0])


p1 = sum(filter(lambda sz: sz <= 100000, list(dirs.values())))

to_delete = 30000000 - (70000000 - dirs['/'])
p2 = next(filter(lambda sz: sz >= to_delete, sorted(dirs.values())))

print(p1)
print(p2)
