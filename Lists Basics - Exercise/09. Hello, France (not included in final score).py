string = input().split('|')
buget = float(input())
b = buget
prof = 0
for i in range(len(string)):
    string[i] = string[i].split('->')
sale = []
for i in range(len(string)):
    if string[i][0] == 'Clothes' and float(string[i][1]) <= 50:
        if float(string[i][1]) <= buget:
            buget -= float(string[i][1])
            sale.append(float(string[i][1])*1.4)
            prof += float(string[i][1])*1.4 - float(string[i][1])
    elif string[i][0] == 'Shoes' and float(string[i][1]) <= 35:
        if float(string[i][1]) <= buget:
            buget -= float(string[i][1])
            sale.append(float(string[i][1])*1.4)
            prof += (float(string[i][1]) * 1.4 - float(string[i][1]))
    elif string[i][0] == 'Accessories' and float(string[i][1]) <= 20.5:
        if float(string[i][1]) <= buget:
            buget -= float(string[i][1])
            sale.append(float(string[i][1])*1.4)
            prof += float(string[i][1]) * 1.4 - float(string[i][1])
for i in sale:
    print('%.2f' % i, end=' ')
print()
print(f'Profit: {prof:.2f}')
if sum(sale)+buget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
