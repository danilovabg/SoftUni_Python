names = input().split(', ')
sort = sorted(names, key=lambda x: (-len(x), x))
print(sort)