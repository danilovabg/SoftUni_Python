import re

apartment_info = input()
app_type_regex = '(\w+)Apartment'
office, living = {}, {}
while apartment_info != 'start_selling':
    app_type = re.findall(app_type_regex, apartment_info)
    info_regex = '\((\".+)\)'
    info = re.findall(info_regex, apartment_info)
    info = info[0].split(', ')
    if len(app_type) == 0:
        print("Can't instantiate abstract class Apartment with abstract methods __str__")
    else:
        if app_type[0] in ['Office', 'Living']:
            if len(info) == 5:
                if app_type[0] == 'Office':
                    office[info[0][1:-1]] = info[1:]
                elif app_type[0] == 'Living':
                    living[info[0][1:-1]] = info[1:]
            elif len(info) < 5:
                print("__init__() missing 1 required positional argument: 'price'")
    apartment_info = input()

taken = []
selling = input()
while selling not in ['taken', 'free']:
    command, app_id = selling.split()
    if app_id in taken:
        print(f"Apartment with id - {app_id} is already taken!")
    elif app_id not in office and app_id not in living:
        print(f"Apartment with id - {app_id} does not exist!")
    else:
        if command == 'rent' and app_id in living:
            print(f"Apartment with id - {app_id} is only for selling!")
        elif command == 'hire' and app_id in office:
           print(f"Apartment with id - {app_id} is only for renting")
        elif command == 'buy' and app_id in living:
            taken.append((app_id, list(map(float, living[app_id]))))
            living.pop(app_id)
        elif command == 'rent' and app_id in office:
            taken.append((app_id, list(map(float, office[app_id]))))
            office.pop(app_id)
        else:
            if app_id in office:
                taken.append((app_id, list(map(float, office[app_id]))))
                office.pop(app_id)
            elif app_id in living:
                taken.append((app_id, list(map(float, living[app_id]))))
                living.pop(app_id)
    selling = input()

if selling == 'taken':
    if len(taken) > 0:
        taken = sorted(taken, key=lambda x: (x[1][3], -x[1][2]))
    else:
        print("No information for this query")

if selling == 'taken':
    for id, info in taken:
        print(f"{int(info[0])} rooms place with {int(info[1])} bathroom/s.\n{info[2]} sq. meters for {info[3]} lv.")
if selling == 'free':
    free =[]
    for el, value in office.items():
        free.append((el, list(map(float, value))))
    for el, value in living.items():
        free.append((el,list(map(float, value))))
    free = sorted(free, key=lambda x: (-x[1][3], x[1][2]))
    for id, info in free:
        print(f"{int(info[0])} rooms place with {int(info[1])} bathroom/s.\n{info[2]} sq. meters for {info[3]} lv.")
    if len(free) == 0:
        print("No information for this query")
# print(office)
# print(living)
# print(taken)