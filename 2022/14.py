from input_utils import get_lines


ROCKS = set()
max_y = 0
for line in get_lines('14.in'):
    points = list(map(eval, line.split(' -> ')))
    x, y = points[0]
    max_y = max(max_y, y)
    ROCKS.add((x, y))
    for (xx, yy) in points[1:]:
        dx = 1 if xx > x else 0 if xx == x else -1
        dy = 1 if yy > y else 0 if yy == y else -1
        for i in range(max(abs(xx - x), abs(yy - y)) + 1):
            ROCKS.add((x + i * dx, y + i * dy))
        x, y = xx, yy
        max_y = max(max_y, y)


for part in [1, 2]:
    SANDS: set[tuple[int, int]] = set()
    x, y = 500, 0
    while (part == 1 and y < max_y) or part == 2:
        moved = False
        for (dx, dy) in [(0, 1), (-1, 1), (1, 1)]:
            xx, yy = x + dx, y + dy
            if (xx, yy) not in ROCKS and \
                    (xx, yy) not in SANDS and \
                    yy < max_y + 2:
                x, y = xx, yy
                moved = True
                break
        if not moved:
            SANDS.add((x, y))
            if (x, y) == (500, 0):
                break
            x, y = 500, 0
    print(len(SANDS))
