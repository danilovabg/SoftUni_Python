line = input().split(' ')
w1 = 0
w2 = 0
for i in range(len(line)):
    line[i] = int(line[i])
for i in range(len(line)//2):
    if line[i] != 0:
        w1 += line[i]
    elif line[i] == 0:
        w1 *= 0.8
for i in range(len(line)-1, len(line) // 2, -1):
    if line[i] != 0:
        w2 += line[i]
    elif line[i] == 0:
        w2 *= 0.8
if w1 > w2:
    print(f'The winner is right with total time: {w2:.1f}')
elif w1 < w2:
    print(f'The winner is left with total time: {w1:.1f}')
