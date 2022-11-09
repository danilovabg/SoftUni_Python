string = list(map(int, input().split(", ")))
beggars = int(input())
new_list = []
for b in range(beggars):
    new_list.append(sum(string[b::beggars]))
print(new_list)






# още едно решение (поствано в джадж)
# s_dic = {}
# end = False
# end_list = []
# for be in range(1, beggars+1):
#     be = 'b'+str(be)
#     s_dic.update({be: 0})
# while end is False:
#     if len(string) <= 0:
#         break
#     else:
#         for j in range(1, beggars+1):
#             if len(string) == 0:
#                 end = True
#                 break
#             else:
#                 k = 0
#                 j = 'b'+str(j)
#                 s_dic[j] += int(string[k])
#                 string.remove(string[k])
#                 end_list = list(s_dic.values())
#     if end:
#         break
# print(end_list)