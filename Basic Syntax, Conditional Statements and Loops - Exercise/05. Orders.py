num = int(input())
s = 0
while num > 0:
    caps_pr = float(input())
    days = int(input())
    ca_day = int(input())
    if 100 < caps_pr < 0.01 or 31 < days < 1 or 2000 < ca_day < 1:
        pass
    elif 100 >= caps_pr >= 0.01 and 31 >= days >= 1 and 2000 >= ca_day >= 1:
        summ = ca_day*caps_pr*days
        print(f'The price for the coffee is: ${summ:.2f}')
        s += summ
    num -= 1
print(f'Total: ${s:.2f}')