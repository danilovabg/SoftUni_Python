shopping_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    comm, prod = command.split(maxsplit=1)
    if comm == 'Urgent' and prod not in shopping_list:
        shopping_list.insert(0, prod)
    if comm == 'Unnecessary':
        if prod in shopping_list:
            shopping_list.remove(prod)
    if comm == 'Correct':
        old, new = prod.split()
        if old in shopping_list:
            ind = shopping_list.index(old)
            shopping_list[ind] = new
    if comm == 'Rearrange' and prod in shopping_list:
        shopping_list.remove(prod)
        shopping_list.insert(len(shopping_list), prod)
    command = input()

print(', '.join(shopping_list))

