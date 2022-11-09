lessons = input().split(', ')
command = input().split(':')
while command[0] != 'course start':
    if command[0] == 'Add':
        if command[1] not in lessons:
            lessons.append(command[1])
    elif command[0] == 'Remove':
        if command[1] in lessons:
            lessons.remove(command[1])
        if (command[1]+'-Exercise') in lessons:
            lessons.remove(command[1]+'-Exercise')
    elif command[0] == 'Insert':
        if command[1] not in lessons:
            lessons.insert(int(command[2]), command[1])
    elif command[0] == 'Swap':
        if command[1] in lessons and command[2] in lessons:
            ind1, ind2 = lessons.index(command[1]), lessons.index(command[2])
            lessons[ind1], lessons[ind2] = lessons[ind2], lessons[ind1]
            les_ex1 = command[1] + '-Exercise'
            les_ex2 = command[2] + '-Exercise'
            if les_ex1 in lessons:
                ind1 = lessons.index(command[1])
                lessons.remove(les_ex1)
                lessons.insert(ind1+1, les_ex1)
            if les_ex2 in lessons:
                ind2 = lessons.index(command[2])
                lessons.remove(les_ex2)
                lessons.insert(ind2+1, les_ex2)
    elif command[0] == 'Exercise':
        if (command[1]+'-Exercise') not in lessons:
            if command[1] in lessons:
                ind = lessons.index(command[1])
                lessons.insert(ind+1, command[1]+'-Exercise')
            else:
                lessons.append(command[1])
                lessons.append(command[1]+'-Exercise')
    command = input().split(':')
a = 0
for i in lessons:
    a += 1
    print(f'{a}.{i}')