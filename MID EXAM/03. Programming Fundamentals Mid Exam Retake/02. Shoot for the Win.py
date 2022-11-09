target = list(map(int, input().split()))
index = input()
shot = 0

while index != 'End':
    index = int(index)
    if len(target) > index >= 0:
        x, target[index] = target[index], -1
        shot += 1
        for i, el in enumerate(target):
            if el > x and el != -1:
                target[i] = el - x
            elif el <= x and el != -1:
                target[i] = el + x
    index = input()


print(f'Shot targets: {shot} ->', *target)