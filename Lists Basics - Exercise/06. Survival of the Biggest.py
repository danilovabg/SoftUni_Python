num_list = input().split(' ')
int_list = []
for j in range(len(num_list)):
    k = int(num_list[j])
    int_list.append(k)
n = int(input())
for i in range(n):
    x = min(int_list)
    int_list.remove(x)
print(*int_list, sep=', ')