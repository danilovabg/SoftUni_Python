product = input()
p_dict = {}
while product != 'buy':
    prod = product.split()
    if prod[0] not in p_dict:
        p_dict[prod[0]] = [float(prod[1]), int(prod[2])]
    else:
        p_dict[prod[0]][0] = float(prod[1])
        p_dict[prod[0]][1] += int(prod[2])
    product = input()

[print(f"{p} -> {s[0]*s[1]:.2f} ") for p,s in p_dict.items()]

