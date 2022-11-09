string = list(input())
new_list = []
n = 0
for ind in range(len(string)):
    new_list.append(string[ind])
    if string[ind] == '>':
        n += int(string[ind+1])
    if n > 0:
        if new_list[-1] != '>':
            new_list.pop(-1)
            n -= 1
print(*new_list, sep = '')