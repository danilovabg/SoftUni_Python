n = int(input())
open = 0
unbal = False
close = 0
for i in range(n):
    symbol = input()
    if len(symbol) == 1:
        if ord(symbol) == 40 and open == 1:
            print('UNBALANCED')
            unbal = True
            break
        elif ord(symbol) == 40:
            open = 1
            close = 0
        elif ord(symbol) == 41 and close >= 1:
            print('UNBALANCED')
            unbal = True
            break
        elif ord(symbol) == 41 and open == 1 and close == 0:
            open = 0
            close = 1
        elif ord(symbol) == 41 and open == 0:
            unbal = True
            print('UNBALANCED')
            break
if unbal is False and n > 0:
    print('BALANCED')