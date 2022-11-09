symbols = input().split()
elements = input()
tryes = 0
while elements != 'end':
    tryes += 1
    id1, id2 = list(map(int, elements.split()))
    if (len(symbols)-1) < id1 or id1 < 0 or (len(symbols)-1) < id2 or id2 < 0 or id1 == id2:
        print('Invalid input! Adding additional elements to the board')
        symbols.insert(len(symbols)//2, '-' + str(tryes) + 'a')
        symbols.insert(len(symbols) // 2, '-' + str(tryes) + 'a')
    else:
        if symbols[id1] == symbols[id2]:
            if id1 > id2:
                a = symbols.pop(id1), symbols.pop(id2)
            else:
                a = symbols.pop(id2), symbols.pop(id1)
            print(f'Congrats! You have found matching elements - {a[0]}!')
        else:
            print('Try again!')
    if len(symbols) == 0:
        print(f'You have won in {tryes} turns!')
        break
    elements = input()

if len(symbols) > 0:
    print(f'Sorry you lose :(')
    print(*symbols)
