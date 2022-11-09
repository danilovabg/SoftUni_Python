line = input().split(' ')
k = int(input())
k_list = []
q = 0
while len(line) > 0:
    q = (k - 1 + q) % len(line)
    k_list.append(int(line[q]))
    line.pop(q)
print(f"[{','.join(str(x) for x in k_list)}]")
