num = int(input())
def tribon(num):
    s = [1]
    while len(s) < num:
        b = s[::-1]
        n = sum(b[:3])
        s.append(n)
    return s
print(*tribon(num))
