n = list(input())
m = []
for i in range(len(n)):
   m.append(int(n[i]))
for i in range(len(n)):
    print(max(m), end = '')
    m.remove(max(m))