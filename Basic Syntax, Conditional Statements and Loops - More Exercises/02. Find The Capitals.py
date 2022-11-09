string = input()
index_list = []
for i in range(len(string)):
    if ord(string[i]) in range(65, 91):
        index_list.append(i)
print(index_list)