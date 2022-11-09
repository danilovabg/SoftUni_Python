dwarf = input()
all_dwarfs = {}
while dwarf != 'Once upon a time':
    d = dwarf.split(' <:> ')
    name = d[0]
    hat = d[1]
    physics = int(d[2])
    if (name, hat) not in all_dwarfs:
        all_dwarfs[(name, hat)] = physics
    else:
        if physics > all_dwarfs[(name, hat)]:
            all_dwarfs[(name, hat)] = physics
    dwarf = input()
# print(all_dwarfs)
hat_count = []
d = list(all_dwarfs.keys())

test_list = []
for el in d:
    count = 0
    for ind in range(len(d)):
        if el[1] == d[ind][1]:
            count += 1
    test_list.append((all_dwarfs[el], count, el[1], el[0]))

s = sorted(test_list, key= lambda x: (-x[0], -x[1]))
# print(s)
[print(f"({el[2]}) {el[3]} <-> {el[0]}") for el in s]