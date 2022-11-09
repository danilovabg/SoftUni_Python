item = input()
item_dict = {}
while item != 'stop':
    quantity = int(input())
    if item not in item_dict:
        item_dict[item] = quantity
    else:
        item_dict[item] += quantity
    item = input()
[print(f"{i} -> {q}") for i, q in item_dict.items()]