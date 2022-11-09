list_of_numbers = list(map(int, input().split()))
command =input()
valid_operation = 0
while command != 'end':
    command = command.split()
    if command[0] == 'swap':
        if 0 <= int(command[1]) < len(list_of_numbers) and 0 <= int(command[2]) < len(list_of_numbers):
            list_of_numbers[int(command[1])], list_of_numbers[int(command[2])] = list_of_numbers[int(command[2])], list_of_numbers[int(command[1])],
        print(list_of_numbers)
        valid_operation += 1
    elif command[0] == 'enumerate_list':
        print(list(enumerate(list_of_numbers)))
        valid_operation += 1
    elif command[0] == 'max':
        print(max(list_of_numbers))
        valid_operation += 1
    elif command[0] == 'min':
        print(min(list_of_numbers))
        valid_operation += 1
    elif command[0] == 'get_divisible':
        division_list = []
        for el in list_of_numbers:
            if el % int(command[2]) == 0:
                division_list.append(el)
        print(division_list)
        valid_operation += 1
    command = input()
print(valid_operation)