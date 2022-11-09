import math
string = input().split(', ')

for index in range(len(string)):
    string[index] = string[index].replace(' ', '')

vin_el = ''
for el in string:
    tot_count_1 = 0
    if len(el) != 20:
        print('invalid ticket')
    elif el.count('@') < 12 and el.count('#') < 12 and el.count('$') < 12 and el.count('^') < 12:
        print(f'ticket "{el}" - no match')
    elif el.count('@') == 20 or el.count('#') == 20 or el.count('$') == 20 or el.count('^') == 20:
        print(f'ticket "{el}" - 10{el[0]} Jackpot!')
    else:
        check = {'@': 0, '#': 0, '$': 0, '^': 0}
        i1, i2 = [], []
        for ind in range(10):
            if el[ind] in check:
                check[el[ind]] += 1
                i1.append((ind, el[ind]))
        for ind in range(10, len(el)):
            if el[ind] in check:
                check[el[ind]] += 1
                i2.append((ind, el[ind]))
        # print(i1, i2)
        # print(check)
        if max(check.values()) >= 12:
            for a,b in check.items():
                if b >= 12:
                    vin_el = a
                    break
            i1_copy, i2_copy = i1.copy(), i2.copy()
            for e in i1_copy:
                if e[1] != vin_el:
                    i1.remove(e)

            for e in i2_copy:
                if e[1] != vin_el:
                    i2.remove(e)
            # print('cleari1', i1)
            # print('cleari2', i2)
            c1 = 0
            for ind in range(len(i1)-1):
                if i1[ind][0] == i1[ind+1][0]-1:
                    c1 += 1
                elif i1[ind][0] != i1[ind+1][0]-1 and c1 < 5:
                    i1 = []
                    break
            c2 = 0
            for ind in range(len(i2)-1):
                if i2[ind][0] == i2[ind+1][0]-1:
                    c2 += 1
                    # print('c2', c)
                elif i2[ind][0] != i2[ind+1][0]-1 and c2 < 5:
                    i2 = []
                    break
            if len(i1) > 0 and len(i2) > 0:
                print(f'ticket "{el}" - {min(c1,c2)+1}{i1[0][1]}')
            else:
                print(f'ticket "{el}" - no match')
