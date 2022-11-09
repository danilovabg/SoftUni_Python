numbers_of_lines = int(input())
battle_firld = []
while numbers_of_lines > 0:
    new_line = list(map(int, input().split()))
    battle_firld.append(new_line)
    numbers_of_lines -= 1
ship_killed = 0
reduce_health = input().split()
for i in range(len(reduce_health)):
    reduce_health[i] = list(map(int, reduce_health[i].split('-')))
for i in range(len(reduce_health)):
    row = reduce_health[i][0]
    col = reduce_health[i][1]
    battle_firld[row][col] -= 1
    if battle_firld[row][col] == 0:
        ship_killed += 1
print(ship_killed)