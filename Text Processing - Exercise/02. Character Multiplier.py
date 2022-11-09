line = input().split()
summ = 0
line.sort(key=lambda el: -len(el))

while len(line[0]) != len(line[1]):
    line[1] = line[1]+chr(1)

for ind in range(len(line[0])):
    summ += ord(line[0][ind])* ord(line[1][ind])

print(summ)