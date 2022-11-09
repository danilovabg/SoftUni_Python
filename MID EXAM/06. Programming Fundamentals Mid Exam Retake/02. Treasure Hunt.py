initial_treasure = input().split('|')

command = input()

while command != 'Yohoho!':
    command = command.split()
    if command[0] == 'Loot':
        for el in command[1:]:
            if el not in initial_treasure:
                initial_treasure.insert(0, el)
    elif command[0] == 'Drop' and 0 <= int(command[1]) < len(initial_treasure)-1:
        x = initial_treasure.pop(int(command[1]))
        initial_treasure.append(x)
    elif command[0] == 'Steal':
        if int(command[1]) < len(initial_treasure):
            print(', '.join(initial_treasure[len(initial_treasure) - int(command[1]):]))
            initial_treasure = initial_treasure[:len(initial_treasure) - int(command[1])]
        else:
            print(', '.join(initial_treasure))
            initial_treasure = []
    command = input()

if len(initial_treasure) > 0:
    x = [len(el) for el in initial_treasure]
    print(f'Average treasure gain: {sum(x)/len(x):.2f} pirate credits.')
else:
    print('Failed treasure hunt.')