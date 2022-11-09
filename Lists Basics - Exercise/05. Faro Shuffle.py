string = input().split(' ')
n = int(input())
first_half = []
second_half = []
for i in range(n):
    for k in range(1, len(string)+1):
        if k <= len(string)/2:
            first_half.append(string[k-1])
        else:
            second_half.append(string[k-1])
    string.clear()
    for j in range(len(first_half)):
        string.append(first_half[j])
        string.append(second_half[j])
    first_half.clear()
    second_half.clear()
print(string)

