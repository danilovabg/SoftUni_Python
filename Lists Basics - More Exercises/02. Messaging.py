line = input().split(' ')
string = list(input())

s = 0
s_list = []
for num in range(len(line)):
    s = 0
    for i in line[num]:
        s += int(i)
    s_list.append(s)
for j in s_list:
    ind = j % len(string)
    print(string[ind], end='')
    string.remove(string[ind])
