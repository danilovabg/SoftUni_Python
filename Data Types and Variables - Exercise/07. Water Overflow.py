n = int(input())
s = 0
if n > 0:
    for i in range(n):
        liter = int(input())
        if s+liter <= 255:
            s += liter
        else:
            print('Insufficient capacity!')
            pass
    print(s)
