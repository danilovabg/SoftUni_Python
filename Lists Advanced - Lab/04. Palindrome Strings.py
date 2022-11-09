string_list = input().split(' ')
pol = input()
polindrom = []
for i in string_list:
    a = list(i)
    x = len(i)//2
    j = 0
    q = 0
    while x > 0:
        if a[j] == a[len(a)-1-j]:
            q += 1
        else:
            break
        if q == len(a)//2:
            polindrom.append(i)
        j += 1
        x -= 1
print(polindrom)
print(f'Found palindrome {polindrom.count(pol)} times')
