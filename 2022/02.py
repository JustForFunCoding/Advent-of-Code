from input_utils import get_lines


# op, me
# A, X - rock
# B, Y - paper
# C, Z - scissors
d1 = {}
d1['A X'] = 4
d1['A Y'] = 8
d1['A Z'] = 3
d1['B X'] = 1
d1['B Y'] = 5
d1['B Z'] = 9
d1['C X'] = 7
d1['C Y'] = 2
d1['C Z'] = 6

# op, end
# A, X - rock, lose
# B, Y - paper, draw
# C, Z - scissors, win
d2 = {}
d2['A X'] = 3
d2['A Y'] = 4
d2['A Z'] = 8
d2['B X'] = 1
d2['B Y'] = 5
d2['B Z'] = 9
d2['C X'] = 2
d2['C Y'] = 6
d2['C Z'] = 7

p1 = p2 = 0
for line in get_lines('02.in'):
    line = line.strip()
    p1 += d1[line]
    p2 += d2[line]

print(p1)
print(p2)
