raw_key = input()

command = input()
while command != 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':
        if command[1] in raw_key:
            print(f'{raw_key} contains {command[1]}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        ind1, ind2 = int(command[2]), int(command[3])
        if ind2 < len(raw_key):
            if command[1] == 'Upper':
                raw_key = raw_key[:ind1]+raw_key[ind1:ind2].upper() + raw_key[ind2:]
            else:
                raw_key = raw_key[:ind1] + raw_key[ind1:ind2].lower() + raw_key[ind2:]
        print(raw_key)
    elif command[0] == 'Slice':
        ind1, ind2 = int(command[1]), int(command[2])
        raw_key = raw_key[:ind1]+raw_key[ind2:]
        print(raw_key)
    command = input()
print(f'Your activation key is: {raw_key}')