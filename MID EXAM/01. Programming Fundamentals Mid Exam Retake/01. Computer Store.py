prices = input()
summ = 0
while prices not in ["special", "regular"]:
    prices = float(prices)
    if prices < 0:
        print("Invalid price!")
    else:
        summ += prices
    prices = input()

if summ == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {summ:.2f}$")
    print(f'Taxes: {summ*0.2:.2f}$\n-----------')
    summ *= 1.2
    if prices == 'special':
        summ *= 0.9
    print(f'Total price: {summ:.2f}$')
