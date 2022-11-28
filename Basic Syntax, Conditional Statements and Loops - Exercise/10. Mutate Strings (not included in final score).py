st1, st2 = input(), input()
y, word = '', st1

if st1 != st2:
    for x in range(1, len(st1)+1):
        y = (st2[0: x] + st1[x:len(st1)])
        if word != y:
            print(y)
            word = y
