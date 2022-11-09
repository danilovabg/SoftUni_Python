#word = input()[::-1]
#print(word)

w = input()
s = ''
for i in range(len(w)-1, -1 ,-1):
    s += w[i]
print(s)