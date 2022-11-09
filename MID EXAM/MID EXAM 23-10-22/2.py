names = input().split(', ')
command = input()
blak_list, lost_names = [], []
while command != 'Report':
    command = command.split()
    if command[0] == 'Blacklist':
        if command[1] in names:
            blak_list.append(command[1])
            print(f'{command[1]} was blacklisted.')
            ind = names.index(command[1])
            names[ind] = 'Blacklisted'
        elif command[1] not in names:
            print(f'{command[1]} was not found.')
    if command[0] == 'Error':
        ind = int(command[1])
        if 0 <= ind < len(names) and names[ind] !='Blacklisted' and names[ind] != 'Lost':
            print(f'{names[ind]} was lost due to an error.')
            lost_names.append(names[ind])
            names[ind] = 'Lost'
    if command[0] == 'Change':
        ind, new_name = int(command[1]), command[2]
        if 0 <= ind < len(names):
            print(f'{names[ind]} changed his username to {new_name}.')
            names[ind] = new_name

    command = input()

print(f'Blacklisted names: {len(blak_list)}')
print(f'Lost names: {len(lost_names)}')
print(*names)