from input_utils import *


lines = get_lines('04.in')


p1 = p2 = 0
for line in lines:
    fst, snd = line.split(',')
    lo1, hi1 = int(fst.split('-')[0]), int(fst.split('-')[1])
    lo2, hi2 = int(snd.split('-')[0]), int(snd.split('-')[1])
    if lo1 <= lo2 <= hi2 <= hi1 or lo2 <= lo1 <= hi1 <= hi2:
        p1 += 1
    if not (hi1 < lo2 or hi2 < lo1):
        p2 += 1


print(p1)
print(p2)
