string, command = input(), input()

while command != 'Done':
    if command == 'TakeOdd':
        string = string[1::2]
        print(string)
    else:
        command = command.split()
        if command[0] == 'Cut':
            string = string[:int(command[1])] + string[int(command[1]) + int(command[2]):]
            print(string)
        elif command[0] == 'Substitute':
            if command[1] in string:
                string = string.replace(command[1], command[2])
                print(string)
            else:
                print('Nothing to replace!')
    command = input()

print(f'Your password is: {string}')