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
        if ord(symbol) == 40:
            open = 1
            close = 0
        if ord(symbol) == 41 and close >= 1:
            print('UNBALANCED')
            unbal = True
            break
        if ord(symbol) == 41 and open == 1 and close == 0:
            open = 0
            close = 1
if unbal == False and n > 0:
    print('BALANCED')