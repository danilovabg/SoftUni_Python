import math
group_size = int(input())
days = int(input())
gold = 0
for i in range(1, days+1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
        gold -= group_size*2
    if i % 3 == 0:
        gold -= group_size*3
    if i % 5 == 0:
        gold += 20*group_size

    gold += 50 - group_size * 2
print(f'{group_size} companions received {math.floor(gold/group_size)} coins each.')


