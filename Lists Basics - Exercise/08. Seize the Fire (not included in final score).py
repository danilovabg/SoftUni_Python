fire_level = input().split('#')
water = int(input())
w = water
effort = 0
cells = []
if water >= 0:
    for i in range(len(fire_level)):
        fire_level[i] = fire_level[i].split(' = ')
    for i in range(len(fire_level)):
        if fire_level[i][0] == 'High' and 81 <= int(fire_level[i][1]) <= 125:
            if water >= int(fire_level[i][1]):
                water -= int(fire_level[i][1])
                effort += int(fire_level[i][1]) * 0.25
                cells.append(int(fire_level[i][1]))
        elif fire_level[i][0] == 'Medium' and 51 <= int(fire_level[i][1]) <= 80:
            if water >= int(fire_level[i][1]):
                water -= int(fire_level[i][1])
                effort += int(fire_level[i][1]) * 0.25
                cells.append(int(fire_level[i][1]))
        elif fire_level[i][0] == 'Low' and 1 <= int(fire_level[i][1]) <= 50:
            if water >= int(fire_level[i][1]):
                water -= int(fire_level[i][1])
                effort += int(fire_level[i][1]) * 0.25
                cells.append(int(fire_level[i][1]))
    print('Cells:')
    if w != 0:
        for n in cells:
            print(f" - {n}")
        print(f'Effort: {effort:.2f}')
        print(f'Total Fire: {sum(cells)}')

