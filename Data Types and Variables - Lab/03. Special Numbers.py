n = int(input())
for num in range(1, n+1):
    summ = num //10 + num % 10
    if summ == 5:
        print(f'{num} -> True')
    elif summ == 7:
        print(f'{num} -> True')
    elif summ == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
