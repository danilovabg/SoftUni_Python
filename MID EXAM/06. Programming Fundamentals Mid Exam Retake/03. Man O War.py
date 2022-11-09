pirat_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
command = input()

sink = False
while command != 'Retire':
    command = command.split()

    if len(command) > 1:
        ind = int(command[1])

        if command[0] == 'Fire' and ind in range(len(warship)):
            warship[ind] -= int(command[2])
            if warship[ind] <= 0:
                print(f'You won! The enemy ship has sunken')
                sink = True
                break
        elif command[0] == 'Defend':
            if ind in range(len(pirat_ship)) and int(command[2]) in range(len(pirat_ship)):
                ind2 = (int(command[2])+1)
                for i in range(ind, ind2):
                    pirat_ship[i] -= int(command[3])
                    if pirat_ship[i] <= 0:
                        print('You lost! The pirate ship has sunken.')
                        sink = True
                        break


        elif command[0] == 'Repair' and ind in range(len(pirat_ship)):
            pirat_ship[ind] += int(command[2])
            if pirat_ship[ind] > max_health:
                pirat_ship[ind] = max_health
    else:
        count = [1 for el in pirat_ship if el < 0.2 * max_health]
        print(f'{len(count)} sections need repair.')

    #print(warsheep_status, pirat_sheep_status)
    command = input()

if sink is False:
    print(f"Pirate ship status: {sum(pirat_ship)}")
    print(f"Warship status: {sum(warship)}")
