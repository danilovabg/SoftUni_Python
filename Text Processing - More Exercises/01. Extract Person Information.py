num = int(input())

while num > 0:
    name = ''
    age = ''
    start_name = False
    start_age = False
    line = input()
    for el in line:
        if start_name and el != '|':
            name += el
        elif el == '|':
            break
        if el == '@':
            start_name = True
    for el in line:
        if start_age and el != '*':
            age += el
        elif el == '*':
            break
        if el == '#':
            start_age = True
    print(f"{name} is {age} years old.")
    num -= 1
