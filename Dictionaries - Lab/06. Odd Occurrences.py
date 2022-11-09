line = input().lower().split()
line_dict = {}
for el in line:
    if line.count(el) % 2 != 0:
        line_dict[el] = int(line.count(el))
print(*line_dict)
