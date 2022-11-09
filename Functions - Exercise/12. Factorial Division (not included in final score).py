n1 = int(input())
n2 = int(input())
def fun(n1, n2):
    s1 = 1
    s2 = 1
    for n in range(1, n1+1):
        s1 *= n
    for n in range(1, n2+1):
        s2 *= n
    res = s1/s2
    return res
print(f'{fun(n1, n2):.2f}')