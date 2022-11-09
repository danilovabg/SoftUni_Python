numbers_of_lines = int(input())
field = []
dots_list = []
#  създавам матрица

while numbers_of_lines > 0:
    new_line = input().split()
    field.append(new_line)
    numbers_of_lines -= 1

# търся координати на всички точки в матрица

for row in range(len(field)):
    for col in range(len(field[row])):
        if field[row][col] == '.':
            dots_list.append([row, col])

# функция която търси всички "свързани" точки от зададен координат

def dots_count_funktion(ind_row, ind_col):
    if 0 <= ind_row < len(field) and 0 <= ind_col < len(field[0]):
        if ind_col < len(field[0])-1:
            if field[ind_row][ind_col+1] == '.' and [ind_row, ind_col+1] not in result:
                result.append([ind_row, ind_col+1])
                dots_count_funktion(ind_row, ind_col+1)
        if ind_col > 0:
            if field[ind_row][ind_col-1] == '.' and [ind_row, ind_col-1] not in result:
                result.append([ind_row, ind_col-1])
                dots_count_funktion(ind_row, ind_col-1)
        if ind_row < len(field)-1:
            if field[ind_row+1][ind_col] == '.' and [ind_row+1, ind_col] not in result:
                result.append([ind_row+1, ind_col])
                dots_count_funktion(ind_row+1, ind_col)
        if ind_row > 0:
            if field[ind_row-1][ind_col] == '.' and [ind_row-1, ind_col] not in result:
                result.append([ind_row-1, ind_col])
                dots_count_funktion(ind_row-1, ind_col)
    return result

# прилагам функция към всички точки от матрица, за да намеря най голямата верига
final_list = []
if len(dots_list) == 0:
    print(0)
else:
    for dot in dots_list:
        result = []
        ind_row = dot[0]
        ind_col = dot[1]
        dots_count_funktion(ind_row, ind_col)
        final_list.append(result)
    print(max(len(x) for x in final_list))

