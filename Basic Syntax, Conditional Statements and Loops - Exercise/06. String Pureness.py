n = int(input())
while n > 0:
    string = input()
    p = 0
    for i in list(string):
        if ord(i) == 44 or ord(i) == 46 or ord(i) == 95:
            p += 1
    if p == 0:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
    n -= 1
