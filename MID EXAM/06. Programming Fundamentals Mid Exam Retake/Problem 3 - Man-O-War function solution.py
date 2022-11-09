def fire(args):

    ind, damage = args
    if ind in range(len(warship)):
        warship[ind] -= damage
        if warship[ind] <= 0:
            print(f'You won! The enemy ship has sunken.')
            return 'end'
        else:
            return warship


def defend(args):

    ind1, ind2, damage = args
    if ind1 in range(len(pirat_ship)) and ind2 in range(len(pirat_ship)):
        if ind1 > ind2:
            ind1, ind2 = ind2, ind1
        for i in range(ind1, ind2+1):
            pirat_ship[i] -= damage
            if pirat_ship[i] <= 0:
                print('You lost! The pirate ship has sunken.')
                return 'end'

        return pirat_ship


def repair(args):

    ind, health = args
    if ind in range(len(pirat_ship)):
        pirat_ship[ind] += health
        if pirat_ship[ind] > max_health:
            pirat_ship[ind] = max_health

        return pirat_ship


def status(max_health):

    count = [1 for el in pirat_ship if el < 0.2 * max_health]
    print(f'{len(count)} sections need repair.')

pirat_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
command = input().split()

while command[0] != 'Retire':
    game = 'on'
    funk = command[0]
    args = [int(x) for x in command[1:]]

    if funk == 'Fire':
        game = fire(args)
    elif funk == 'Defend':
        game = defend(args)
    elif funk == 'Repair':
        repair(args)
    elif funk == 'Status':
        status(max_health)
    if game == 'end':
        break
    command = input().split()

if command[0] == 'Retire':
    print(f"Pirate ship status: {sum(pirat_ship)}")
    print(f"Warship status: {sum(warship)}")
