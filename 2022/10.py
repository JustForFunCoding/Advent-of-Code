from input_utils import *


lines = get_lines('10.in')
X = 1
round_num = signal_strength = 0
linebreaking_rounds = [x for x in range(20, 221, 40)]
G = [['?' for _ in range(40)] for _ in range(6)]


def handle_tick() -> None:
    global round_num, X, signal_strength
    G[round_num//40][round_num % 40] = '#' if abs(X - (round_num % 40)) <= 1 else ' '
    round_num += 1
    if round_num in linebreaking_rounds:
        signal_strength += X * round_num


for cmd in lines:
    words = cmd.split(' ')
    op = words[0]
    if op == 'noop':
        handle_tick()
    elif op == 'addx':
        handle_tick()
        handle_tick()
        X += int(words[1])

print(signal_strength)
for r in range(6):
    print(''.join(G[r]))
