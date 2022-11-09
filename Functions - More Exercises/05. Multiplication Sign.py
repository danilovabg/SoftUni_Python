n1 = int(input())
n2 = int(input())
n3 = int(input())
def mult(n1, n2, n3):
    q = 0
    if n1 == 0 or n2 == 0 or n3 == 0:
        res = 'zero'
    else:
        if n1 < 0:
            q += 1
        if n2 < 0:
            q += 1
        if n3 < 0:
            q += 1
        if q == 0 or q == 2:
            res = 'positive'
        else:
            res = 'negative'
    return res
print(mult(n1, n2, n3))