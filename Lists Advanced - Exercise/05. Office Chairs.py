rooms = int(input())
cl = []
x = 2
while rooms > 0:
    cl.append(input().split(' '))
    rooms -= 1
test = list(map(lambda i: (len(cl[i][0])-int(cl[i][1])) if len(cl[i][0]) >= int(cl[i][1]) else f'{int(cl[i][1])-len(cl[i][0])} more chairs needed in room {i+1}', range(len(cl))))
try:
    print(f'Game On, {sum(test)} free chairs left')
except TypeError:
    for el in test:
        if type(el) is str:
            print(el)
