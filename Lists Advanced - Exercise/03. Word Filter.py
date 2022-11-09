string = input().split()
new_list = []
[new_list.append(x) for x in string if len(x) % 2 == 0 if x not in new_list]
print(*new_list, sep='\n')