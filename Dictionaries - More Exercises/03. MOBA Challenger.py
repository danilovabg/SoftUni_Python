line = input()
pool = {}
stop = False

while line != 'Season end':
    if ' -> ' in line:
        l = line.split(' -> ')
        name = l[0]
        position = l[1]
        points = int(l[2])
        if name not in pool:
            pool[name] = {position: points}
        else:
            if position not in pool[name]:
                pool[name][position] = points
            else:
                if pool[name][position] < points:
                    pool[name][position] = points
    elif ' vs ' in line:
        l = line.split(' vs ')
        player1 = l[0]
        player2 = l[1]
        if player1 and player2 in pool:
            for key1 in pool[player1].keys():
                if key1 in pool[player2].keys():
                    stop = True
                    if sum(pool[player1].values()) > sum(pool[player2].values()):
                        pool.pop(player2)
                    elif sum(pool[player1].values()) < sum(pool[player2].values()):
                        pool.pop(player1)
                    break
                if stop:
                    break
    # print(pool)
    line = input()


new = []
for player, score in pool.items():
    new.append((player, sum(score.values())))
new.sort(key=lambda x: (-x[1], x[0]))

for el in new:
    print(f"{el[0]}: {el[1]} skill")
    s = sorted(pool[el[0]].items(), key=lambda item: (-item[1], item[0]))
    for el in s:
        print(f"- {el[0]} <::> {el[1]}")
