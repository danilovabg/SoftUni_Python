gifts_list = input().split(' ')
command = input().split(' ')
while command != 'No Money':
    if command[0] == 'OutOfStock':
        for g in range(len(gifts_list)):
            if gifts_list[g] == command[1]:
                gifts_list[gifts_list.index(command[1])] = 'None'
    elif command[0] == 'Required':
        if len(gifts_list) > int(command[2]) and int(command[2]) >= 0:
            gifts_list[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        gifts_list[len(gifts_list)-1] = command[1]
    command = input().split(' ')
    if command[0] == 'No' and command[1] == 'Money' and len(command) == 2:
        break
while 'None' in gifts_list:
    gifts_list.remove('None')
print(*gifts_list)
