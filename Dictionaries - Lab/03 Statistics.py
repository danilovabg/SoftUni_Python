
line = input()
stat_dict = {}
while line != 'statistics':
    elem = line.split(': ')
    if elem[0] in stat_dict:
        stat_dict[elem[0]] += int(elem[1])
    else:
        stat_dict[elem[0]] = int(elem[1])
    line = input()
print("Products in stock:")
[print(f"- {p}: {q}") for (p, q) in stat_dict.items()]

print(f'Total Products: {len(stat_dict)}')
print(f'Total Quantity: {sum(stat_dict.values())}')
