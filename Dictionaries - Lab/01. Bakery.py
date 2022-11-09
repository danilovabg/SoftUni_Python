line = input().split()
line_dict = {}
for i in range(0, len(line), 2):
    key = line[i]
    val = line[i+1]
    line_dict[key] = int(val)

print(line_dict)

#  ПОЧЕМУ НЕ РАБОТАЕТ?????
# line = input().split()
# line_dict = {}
# for el in line[::2]:
#     ind = 1 + line.index(el)
#     line_dict[el] = int(line[ind])
#
# print(line_dict)
