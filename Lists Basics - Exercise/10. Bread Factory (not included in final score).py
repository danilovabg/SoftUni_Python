bakery = input().split('|')
coins = 100
energy = 100
closed = False
for i in range(len(bakery)):
    bakery[i] = bakery[i].split('-')
for i in range(len(bakery)):
    if bakery[i][0] == 'rest':
        if energy+int(bakery[i][1]) <= 100:
            energy += int(bakery[i][1])
            diff = int(bakery[i][1])
        elif energy == 100:
            diff = 0
        else:
            diff = 100 - energy
            energy = 100
        print(f'You gained {diff} energy.')
        print(f'Current energy: {energy}.')
    elif bakery[i][0] == 'order':
        if energy >= 30:
            coins += int(bakery[i][1])
            energy -= 30
            print(f'You earned {bakery[i][1]} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if int(bakery[i][1]) <= coins:
            print(f'You bought {bakery[i][0]}.')
            coins -= int(bakery[i][1])
        else:
            print(f'Closed! Cannot afford {bakery[i][0]}.')
            closed = True
            break
    if closed:
        break
if not closed:
    print("Day completed!")
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
