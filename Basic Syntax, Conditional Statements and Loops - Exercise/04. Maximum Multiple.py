devis = int(input())
frange = int(input())
num = []
for i in range(1, frange+1):
    if i % devis == 0:
        num.append(i)
print(max(num))