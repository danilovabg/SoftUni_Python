command = input()
cities = {}
while command != 'Sail':
    city, population, gold = command.split("||")
    if city in cities:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)
    else:
        cities[city] = [int(population), int(gold)]
    command = input()

action = input()
while action != 'End':
    action = action.split('=>')
    if action[0] == 'Plunder':
        town, people, gold = action[1], int(action[2]), int(action[3])
        if town in cities:
            if people < cities[town][0] and gold < cities[town][1]:
                cities[town][0] -= people
                cities[town][1] -= gold
                print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
            else:
                diff_people = people if cities[town][0] >= people else cities[town][0]
                diff_gold = gold if cities[town][1] >= gold else cities[town][1]
                print(f'{town} plundered! {diff_gold} gold stolen, {diff_people} citizens killed.')
                print(f'{town} has been wiped off the map!')
                cities.pop(town)
    elif action[0] == 'Prosper':
        town, gold = action[1], int(action[2])
        if town in cities:
            if gold > 0:
                cities[town][1] += gold
                print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
            else:
                print(f'Gold added cannot be a negative number!')
    action = input()
if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    [print(f'{town} -> Population: {cities[town][0]} citizens, Gold: {cities[town][1]} kg') for town in cities]
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')