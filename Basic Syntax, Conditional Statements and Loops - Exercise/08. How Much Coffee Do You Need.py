ev = ['cat', 'dog', 'coding', 'movie']
EV = ['CAT', 'DOG', 'CODING', 'MOVIE']
coffee = 0
event = input()
while event != 'END':
    if event in ev:
        coffee += 1
    elif event in EV:
        coffee += 2
    else:
        pass
    event = input()
if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)

