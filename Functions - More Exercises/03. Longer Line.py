import math

x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
y3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y4 = math.floor(float(input()))
def longer(x1, x2, x3, x4, y1 ,y2, y3, y4):
    h1 = ((x2-x1)**2 + (y2-y1)**2)**1/2
    h2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 1 / 2
    if h1 >= h2:
        h11 = (x1**2 + y1**2)**1/2
        h12 = (x2**2 + y2**2)**1/2
        if h11 > h12:
            return [(x2, y2), (x1, y1)]
        else:
            return [(x1, y1), (x2, y2)]
    else:
        h13 = (x3 ** 2 + y3 ** 2) ** 1 / 2
        h14 = (x4 ** 2 + y4 ** 2) ** 1 / 2
        if h13 > h14:
            return [(x4, y4), (x3, y3)]
        else:
            return [(x3, y3), (x4, y4)]

print(*longer(x1, x2, x3, x4, y1 ,y2, y3, y4), sep='')