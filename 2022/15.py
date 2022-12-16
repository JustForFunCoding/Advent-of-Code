from input_utils import get_lines


lines = get_lines('15.in')
NOT_BEACON = set()
for line in lines:
    words = line.split(' ')
    sx = int(words[2].split('=')[1][:-1])
    sy = int(words[3].split('=')[1][:-1])
    bx = int(words[8].split('=')[1][:-1])
    by = int(words[9].split('=')[1])
    dist = abs(sx - bx) + abs(sy - by)

    if abs(sy - 2_000_000) > dist:
        continue

    cnt = dist - abs(sy - 2_000_000)
    for i in range(cnt + 1):
        NOT_BEACON.add((sx + i, 2_000_000))
        NOT_BEACON.add((sx - i, 2_000_000))
    if (bx, by) in NOT_BEACON:
        NOT_BEACON.remove((bx, by))

print(len([(x, y) for (x, y) in NOT_BEACON if y == 2_000_000]))
