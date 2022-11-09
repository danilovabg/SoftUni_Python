passw = list(input())
elem = []
for i in range(48, 58):
    elem.append(i)
for i in range(65, 91):
    elem.append(i)
for i in range(97, 123):
    elem.append(i)
def valid(passw):
    a = ''
    b = ''
    c = ''
    if 6 > len(passw) or len(passw) > 10:
        a = 'Password must be between 6 and 10 characters'
    for i in passw:
        if ord(i) not in elem:
            b = 'Password must consist only of letters and digits'
    q = 0
    for i in passw:
        if ord(i) in range(48, 58):
            q += 1
    if q < 2:
        c = 'Password must have at least 2 digits'
    return [a, b, c]
v = 0
for elem in valid(passw):
    if elem != '':
        print(elem)
    else:
        v += 1
    if v == 3:
        print('Password is valid')
