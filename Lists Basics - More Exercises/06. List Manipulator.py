num_list = input().split(' ')
for n in range(len(num_list)):
    num_list[n] = int(num_list[n])
command = input()
odd = []
even = []
res = 0
while command != 'end':
    command = command.split(' ')
    if command[0] == 'exchange':
        if 0 <= int(command[1]) < len(num_list):
            a = num_list[:int(command[1])+1]
            b = num_list[int(command[1])+1:]
            num_list.clear()
            num_list.extend(b)
            num_list.extend(a)
        else:
            print('Invalid index')
    else:
        even.clear()
        odd.clear()
        for i in num_list:
            if int(i) % 2 == 0:
                even.append(i)
            elif int(i) % 2 == 1:
                odd.append(i)
        if command[0] == 'max':
            if command[1] == 'even':
                if len(even) == 0:
                    print('No matches')
                else:
                    for i, num in enumerate(num_list):
                        if num == max(even):
                            res = i
                    print(res)
            elif command[1] == 'odd':
                if len(odd) == 0:
                    print('No matches')
                else:
                    for i, num in enumerate(num_list):
                        if num == max(odd):
                            res = i
                    print(res)
        if command[0] == 'min':
            if command[1] == 'even':
                if len(even) == 0:
                    print('No matches')
                else:
                    for i, num in enumerate(num_list):
                        if num == min(even):
                            res = i
                    print(res)
            elif command[1] == 'odd':
                if len(odd) == 0:
                    print('No matches')
                else:
                    for i, num in enumerate(num_list):
                        if num == min(odd):
                            res = i
                    print(res)
        if command[0] == 'first':
            if command[2] == 'even':
                if int(command[1]) > len(num_list):
                    print('Invalid count')
                else:
                    print(even[:int(command[1])])
            elif command[2] == 'odd':
                if int(command[1]) > len(num_list):
                    print('Invalid count')
                else:
                    print(odd[:int(command[1])])
        if command[0] == 'last':
            if command[2] == 'even':
                if int(command[1]) > len(num_list):
                    print('Invalid count')
                else:
                    print(even[-int(command[1]):])
            elif command[2] == 'odd':
                if int(command[1]) > len(num_list):
                    print('Invalid count')
                else:
                    print(odd[-int(command[1]):])
    command = input()
print(num_list)
