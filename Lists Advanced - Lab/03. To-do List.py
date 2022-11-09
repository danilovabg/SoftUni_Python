todo_list = [0]*10
while True:
    do = input()
    if do == 'End':
        break
    todo = do.split('-')
    ind = int(todo[0])-1
    note = todo[1]
    todo_list.pop(ind)
    todo_list.insert(ind, note)
result = [el for el in todo_list if el != 0]
print(result)
