comp_dict = {}
company = input()
while company != 'End':
    element = company.split(' -> ')
    if element[0] in comp_dict:
        if element[1] not in comp_dict[element[0]]:
            comp_dict[element[0]].append(element[1])
    else:
        comp_dict[element[0]] = [element[1]]
    company = input()


for c, e in comp_dict.items():
    print(c)
    [print(f"-- {emp}") for emp in e]