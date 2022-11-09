num_of_lines = int(input())
maze = [list(input()) for x in range(num_of_lines)]

# търсим начални координати (положението на Кейт в мазето)
for line in maze:
    for j in maze:
        try:
            ind_col_k = line.index('k')
            ind_row_k = maze.index(line)
            break
        except ValueError:
            pass

# търся всички праздни места в мазето на които Кейто потенциално може да стъпи
empty_space = []
for line in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[line][col] == ' ':
            empty_space.append((line, col))

# задавам началната координата
way = [[(ind_row_k, ind_col_k)]]

# в този лист ще слагам координати на пътя, когато вече няма да можем да направим никаква стъпка
# или изход или deadend
done = []
while True:

    for el in way:
        right, left, up, down = False, False, False, False
        ind_row, ind_col = el[-1][0], el[-1][1]
        new_way1, new_way2, new_way3 = el.copy(), el.copy(), el.copy()
        if ind_col+1 < len(maze[0]) and (ind_row, ind_col+1) in empty_space and (ind_row, ind_col+1) not in el:
            el.append((ind_row, ind_col+1))
            right = True # направена стъпка в дясну
        if ind_col-1 < len(maze[0]) and (ind_row, ind_col-1) in empty_space \
                and el + [(ind_row, ind_col-1)] not in way and (ind_row, ind_col-1) not in el:
            if right is False:
                el.append((ind_row, ind_col - 1))
            else:
                new_way1.append((ind_row, ind_col-1))
                way.append(new_way1)
            left = True  # направена стъпка в ляво
        if ind_row+1 < len(maze) and (ind_row+1, ind_col) in empty_space \
                and el + [(ind_row+1, ind_col)] not in way and (ind_row+1, ind_col) not in el:
            if right is False and left is False:
                el.append((ind_row+1, ind_col))
            else:
                new_way2.append((ind_row+1, ind_col))
                way.append(new_way2)
            down = True  # направена стъпка долу
        if ind_row-1 >= 0 and (ind_row-1, ind_col) in empty_space \
                and el + [(ind_row-1, ind_col)] not in way and (ind_row-1, ind_col) not in el:
            if right is False and left is False and up is False:
                el.append((ind_row-1, ind_col))
            else:
                new_way3.append((ind_row-1, ind_col))
                way.append(new_way3)
            up = True  # направена стъпка на горе

        if left is False and right is False and up is False and down is False:
            done.append(el)
            way.remove(el)
            break # ако вече не можем да стъпим никъде - добавям път в списък done
            # и махаме от списъка в който още търсиме варианти на движение по лабиринта
    if len(way) == 0:
        break #ако проверихме всички възможно пътища - спираме цикъл

longest_way = [len(x) for x in done if x[-1][0] in [0, len(maze)-1] or x[-1][1] in [len(maze[0])-1, 0]]

if len(longest_way) == 0:
    print('Kate cannot get out')
else:
    print(f'Kate got out in {max(longest_way)} moves')

# for el in maze:
#     print(el)
