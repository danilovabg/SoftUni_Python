string = input().split(', ')
n = string.count('0')
for n in range(n):
    string.remove('0')
    string.append('0')
for i in range(len(string)):
    string[i] = int(string[i])
print(string)