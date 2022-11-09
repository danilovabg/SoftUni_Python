string = input().split()
command = input().split()
a = int(command[1])
b = int(command[2])
def merge(a, b):
    ind_list = []
    if a < 0:
        a = 0
    if b >= len(string):
        b = len(string)-1
    for i in range(a+1, b+1):
        string[a] += (string[i])
        ind_list.append(i)
    while len(ind_list) > 0:
        string.pop(ind_list[len(ind_list) - 1])
        ind_list.pop(len(ind_list) - 1)
    return string
def divide(a, b):
    h = len(string[a]) // b
    st = string.pop(a)
    res = []
    for x in range(b - 1):
        res.append(st[:h])
        st = st[h:]
    res.append(st)
    for x in res[::-1]:
        string.insert(a, x)
while command[0] != '3:1':
    a = int(command[1])
    b = int(command[2])
    if command[0] == 'divide':
        divide(a, b)
    elif command[0] == 'merge':
        if a < len(string)-1:
            merge(a, b)
    command = input().split()
print(*string)