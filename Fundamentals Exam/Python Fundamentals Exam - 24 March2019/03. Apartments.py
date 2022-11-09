new_data = input()
data_dict = {}
while new_data != "collectApartments":
    new_data = new_data.split(' -> ')
    if new_data[0] not in data_dict:
        data_dict[new_data[0]] = ({int(x): [] for x in new_data[1].split(',')})
    else:
        buildings = list(map(int, new_data[1].split(',')))
        for num in buildings:
            if num not in data_dict[new_data[0]]:
                data_dict[new_data[0]][num] = []
    new_data = input()

assign = input()
while assign != 'report':
    assign = assign.split(' -> ')
    area, building = assign[0].split('&')
    if area in data_dict and int(building) in data_dict[area]:
        data_dict[area][int(building)] = [assign[1]]
    assign = input()
sorted_data_dict = sorted(data_dict)


for el, b in data_dict.items():
    data_dict[el] = sorted(b.items())

final_tuple = sorted(data_dict.items())

for area in final_tuple:
    print(f"Neighborhood: {area[0]}")
    for build in area[1]:
        if len(build[1]) > 0:
            for el in build[1]:
                app, price = el.split("|")
                print(f"* Block number: {build[0]} -> {app} apartments for sale. Price for one: {price}")
        else:
            print(f"* Block number: {build[0]} -> 0 apartments for sale. Price for one: None")


