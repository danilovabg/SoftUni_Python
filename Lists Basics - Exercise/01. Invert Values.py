string = input()
string = string.split(' ')
str_opposite = []
for i in string:
    i = int(i)
    i = -1*i
    str_opposite.append(i)
print(str_opposite)
