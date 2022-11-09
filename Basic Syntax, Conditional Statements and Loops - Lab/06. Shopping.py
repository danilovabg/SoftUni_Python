end = False
buget = float(input())
price = input()
while price != 'End':
    price = float(price)
    if price > buget:
        print(f'You went in overdraft!')
        break
    buget -= price
    price = input()
    if price == 'End':
        end = True
        break
if end:
    print(f'You bought everything needed.')
