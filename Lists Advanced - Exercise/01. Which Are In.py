list_one, list_two = input().split(", "), input().split(", ")

result_list = list()
[result_list.append(n) for n in list_one for i in list_two if n in i]
result_list = list(dict.fromkeys(result_list))
print(result_list)