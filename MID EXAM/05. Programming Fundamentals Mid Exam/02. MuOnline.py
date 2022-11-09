health, bitcoins = 100, 0
rooms = input().split('|')

room_number = 0
died = False
for room in rooms:
    room_number += 1
    act, num = room.split()
    if act == 'potion':
        if int(num) + health > 100:
            print(f'You healed for {100 - health} hp.')
            health = 100
        else:
            print(f'You healed for {num} hp.')
            health += int(num)
        print(f'Current health: {health} hp.')
    if act == 'chest':
        bitcoins += int(num)
        print(f"You found {num} bitcoins.")
    if act not in ['chest', 'potion']:
        health -= int(num)
        if health > 0:
            print(f"You slayed {act}.")
        else:
            print(f"You died! Killed by {act}.\nBest room: {room_number}")
            died = True
            break

if died is False:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
