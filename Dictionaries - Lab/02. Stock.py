line = input().split()
line_dict = {}
for i in range(0, len(line), 2):
    key = line[i]
    val = line[i+1]
    line_dict[key] = int(val)

order = input().split()
for i in order:
    if i in line_dict:
        print(f"We have {line_dict[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
