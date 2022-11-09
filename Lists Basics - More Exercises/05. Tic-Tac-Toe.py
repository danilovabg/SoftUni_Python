line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')
win = False
try:
    if line1.count('1') == 3 or line2.count('1') == 3 or line3.count('1') == 3:
        print('First player won')
        win = True
except ValueError as e:
    pass
try:
    if line1.count('2') == 3 or line2.count('2') == 3 or line3.count('2') == 3:
        print('Second player won')
        win = True
except ValueError as e:
    pass
try:
    if line1.index('1') == line2.index('1') == line3.index('1'):
        print('First player won')
        win = True
except ValueError as e:
    pass
try:
    if line1.index('2') == line2.index('2') == line3.index('2'):
        print('Second player won')
        win = True
except ValueError as e:
    pass
try:
    if line1[0] == line2[1] == line3[2]:
        if line2[1] == '1':
            print('First player won')
            win = True
        elif line2[1] == '2':
            print('Second player won')
            win = True
    elif line1[2] == line2[1] == line3[0]:
        if line2[1] == '1':
            print('First player won')
            win = True
        elif line2[1] == '2':
            print('Second player won')
            win = True
except ValueError as e:
    pass
if win is False:
    print('Draw!')