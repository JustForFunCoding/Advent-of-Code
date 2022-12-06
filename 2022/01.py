from input_utils import get_number_groups


ng = get_number_groups('01.in')
ssg = sorted(map(lambda arr: sum(arr), ng))

print(ssg[-1])          # part 1
print(sum(ssg[-3:]))    # part 2
