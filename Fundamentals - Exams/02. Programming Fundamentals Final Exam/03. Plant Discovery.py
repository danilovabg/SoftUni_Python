n = int(input())
plant_dist = {}

for i in range(n):
    plant, rarity = input().split('<->')
    plant_dist[plant] = [rarity]

action = input()
while action != 'Exhibition':
    action = action.split(': ')
    if action[0] == 'Rate':
        plant, info = action[1].split(' - ')
        if plant in plant_dist:
            plant_dist[plant].append(info)
    elif action[0] == 'Update':
        plant, info = action[1].split(' - ')
        if plant in plant_dist:
            plant_dist[plant][0] = info
    elif action[0] == 'Reset':
        plant = action[1]
        if plant in plant_dist:
            plant_dist[action[1]] = plant_dist[action[1]][:1]
    if plant not in plant_dist:
        print('error')
    action = input()


print('Plants for the exhibition:')

for el, info in plant_dist.items():
    rating = [int(x) for x in info[1:] if len(info) > 1]
    if len(rating) == 0:
        print(f'- {el}; Rarity: {info[0]}; Rating: 0.00')
    else:
        print(f'- {el}; Rarity: {info[0]}; Rating: {sum(rating)/len(rating):.2f}')