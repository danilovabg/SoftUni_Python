n = int(input())
shels = [2*x**2 for x in range(1, n)]
electr = []
i = 0
while True:
    if shels[i] < n:
        electr.append(shels[i])
        n -= shels[i]
        i += 1
    elif shels[i] >= n:
        electr.append(n)
        break
print(electr)
