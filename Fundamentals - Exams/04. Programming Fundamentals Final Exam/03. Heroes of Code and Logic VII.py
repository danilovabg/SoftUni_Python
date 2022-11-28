n = int(input())
heroes = {}

for i in range(n):
    name, hp, mp = input().split()
    heroes[name] = [int(hp), int(mp)]

command = input()
while command != 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        if int(command[2]) <= heroes[command[1]][1]:
            heroes[command[1]][1] -= int(command[2])
            print(f'{command[1]} has successfully cast {command[3]} and now has {heroes[command[1]][1]} MP!')
        else:
            print(f'{command[1]} does not have enough MP to cast {command[3]}!')
            # heroes[command[1]][1] = 0
    elif command[0] == 'TakeDamage':
        heroes[command[1]][0] -= int(command[2])
        if heroes[command[1]][0] > 0:
            print(f'{command[1]} was hit for {command[2]} HP by {command[3]} and now has {heroes[command[1]][0]} HP left!')
        else:
            heroes[command[1]][0] = 0
            print(f'{command[1]} has been killed by {command[3]}!')
    elif command[0] == 'Recharge':
        if heroes[command[1]][1] + int(command[2]) > 200:
            diff = 200 - heroes[command[1]][1]
            heroes[command[1]][1] = 200
            print(f'{command[1]} recharged for {diff} MP!')
        else:
            heroes[command[1]][1] += int(command[2])
            print(f'{command[1]} recharged for {command[2]} MP!')
    elif command[0] == 'Heal':
        if heroes[command[1]][0] + int(command[2]) > 100:
            diff = 100 - heroes[command[1]][0]
            heroes[command[1]][0] = 100
            print(f'{command[1]} healed for {diff} HP!')
        else:
            heroes[command[1]][0] += int(command[2])
            print(f'{command[1]} healed for {command[2]} HP!')
    command = input()

for name, info in heroes.items():
    if info[0] > 0:
        print(f'{name}\n  HP: {info[0]}\n  MP: {info[1]}')