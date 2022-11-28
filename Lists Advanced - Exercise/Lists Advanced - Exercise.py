'''02. Next Version'''
n1, n2, n3 = map(int, input().split('.'))
if n3 < 9:
    n3 += 1
else:
    if n2 < 9:
        n2 += 1
        n3 = 0
    else:
        n1+=1
        n2 = 0
        n3 = 0
print(f'{n1}.{n2}.{n3}')