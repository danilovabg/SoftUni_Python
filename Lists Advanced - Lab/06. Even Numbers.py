# num = input().split(', ')
# ind_list = []
# for i, number in enumerate(num):
#     if int(number) % 2 == 0:
#         ind_list.append(i)
# print(ind_list)
num = list(map(int, input().split(', ')))
ind = []
found_ind = map(lambda i: i if num[i] % 2 == 0 else 'no', range(len(num)))
even_ind = list(filter(lambda el: el != 'no', found_ind))
print(even_ind)