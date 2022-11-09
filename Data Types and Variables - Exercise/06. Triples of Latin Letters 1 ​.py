n = int(input())
j = 0
m = 0
k = 0
ch = 0
qa = 0
a = 0
while a < n**3:
    print(chr(97+j), chr(97+k), chr((97+m)), sep='', end='\n')
    if k == n - 1 and m == n - 1:
        qa = 1
        k = 0
    if m < n-1:
        m += 1
    elif m == n-1:
        ch = 1
        m = 0
    if ch > 0 and k < n-1:
        k += 1
        if ch > 0 and qa > 0 and j < n-1:
            j+= 1
            ch = 0
            qa = 0
            k = 0
            m = 0
        ch = 0
    a += 1


