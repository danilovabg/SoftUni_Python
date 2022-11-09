line = input()

while line != 'stop playing':
    line = list(map(int, line.split()))
    unique = True

    for el in line:
        if line.count(el) > 1:
            unique = False
            break
    if unique:
        line_unique = list(map(lambda x: x + 2 if x % 2 == 0 else x, line))
        final_list = sorted(line_unique)
        print('Unique list:', end=' ')
        print(*final_list, sep=',')
        print(f"Output:{sum(final_list)/len(final_list): .2f}")
    else:
        line_not_unique = list(map(lambda x: x + 3 if x % 2 == 1 else x, line))
        final_list = sorted(line_not_unique)
        print('Non-unique list:', end=' ')
        print(*final_list, sep=':')
        print(f"Output:{sum(final_list) / len(final_list): .2f}")
    line = input()