import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
def coord(x1, x2, y1, y2):
    x1 = math.floor(x1)
    x2 = math.floor(x2)
    y1 = math.floor(y1)
    y2 = math.floor(y2)
    h1 = (x1**2 + y1**2) ** 1/2
    h2 = (x2**2 + y2**2) ** 1/2
    if h1 <= h2:
        res = (x1, y1)
    else:
        res = (x2, y2)
    return res
print(coord(x1, x2, y1, y2))