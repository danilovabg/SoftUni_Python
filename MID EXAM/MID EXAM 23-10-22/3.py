book_shelf = input().split('&')

command = input()

while command != 'Done':
    command = command.split(' | ')
    if command[0] == 'Add Book' and command[1] not in book_shelf:
        book_shelf.insert(0, command[1])
    if command[0] == 'Take Book' and command[1] in book_shelf:
        book_shelf.remove(command[1])
    if command[0] == 'Swap Books' and command[1] in book_shelf and command[2] in book_shelf:
        ind1, ind2 = book_shelf.index(command[1]), book_shelf.index(command[2])
        book_shelf[ind1], book_shelf[ind2] = book_shelf[ind2], book_shelf[ind1]
    if command[0] == 'Insert Book' and command[1] not in book_shelf:
        book_shelf.append(command[1])
    if command[0] == 'Check Book' and 0 <= int(command[1]) < len(book_shelf):
        print(book_shelf[int(command[1])])
    command = input()

print(', '.join(book_shelf))