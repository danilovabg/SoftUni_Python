
def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True


def check_wall(row, col):
    if lab[row][col] == "#":
        return True


def check_already_visit(row, col):
    if lab[row][col] == "v":
        return True


def find_exit(row, col):
    if row == 0 or row == len(lab) - 1 or col == 0 or col == len(lab[0]):
        return True


def find_starting_point():
    for pos_row, row in enumerate(lab):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return

    path_steps.append(1)
    if find_exit(row, col):
        max_len_path.append(sum(path_steps))

    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)  # check right
    find_the_lab_path(row, col - 1, lab)  # check left
    find_the_lab_path(row + 1, col, lab)  # check up
    find_the_lab_path(row - 1, col, lab)  # check down
    lab[row][col] = " "

    path_steps.pop()


row = int(input())
lab = []
path_steps = []
max_len_path = []
for _ in range(row):
    lab.append(list(input()))
col = len(lab[0])
start_row, start_col = find_starting_point()

find_the_lab_path(start_row, start_col, lab)

if max_len_path:
    print(f"Kate got out in {max(max_len_path)} moves")
else:
    print("Kate cannot get out")





