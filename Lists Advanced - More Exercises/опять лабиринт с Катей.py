n = int(input())
lab = []
while n > 0:
    line = list(input())
    lab.append(line)
    n -= 1
for line in lab:
    for j in line:
        try:
            ind_col_k = line.index('k')
            ind_row_k = lab.index(line)
            break
        except ValueError:
            pass
print(*lab, sep='\n')
step = []
result = []
res = []
def right_step(ind_row, ind_col):
    if ind_col < len(lab[0]) - 1:
        if lab[ind_row][ind_col + 1] == ' ' and [ind_row, ind_col + 1] not in res:
            res.append([ind_row, ind_col + 1])
            result.append([ind_row, ind_col + 1])

def left_step(ind_row, ind_col):
    if ind_col > 0:
        if lab[ind_row][ind_col - 1] == ' ' and [ind_row, ind_col - 1] not in res:
            res.append([ind_row, ind_col - 1])
            result.append([ind_row, ind_col - 1])

def up_step(ind_row, ind_col):
    if ind_row > 0:
        if lab[ind_row - 1][ind_col] == ' ' and [ind_row - 1, ind_col] not in res:
            res.append([ind_row - 1, ind_col])
            result.append([ind_row - 1, ind_col])

def down_step(ind_row, ind_col):
    if ind_row < len(lab) - 1:
        if lab[ind_row + 1][ind_col] == ' ' and [ind_row + 1, ind_col] not in res:
            res.append([ind_row + 1, ind_col])
            result.append([ind_row + 1, ind_col])

def way(ind_row, ind_col):
    res.clear()
    right_step(ind_row, ind_col)
    left_step(ind_row, ind_col)
    up_step(ind_row, ind_col)
    down_step(ind_row, ind_col)

way(ind_row = ind_row_k, ind_col=ind_col_k)

result = list(filter(lambda el: el != 0, result))
res = []
print('first step 2', result)
first_step = result
all_ways = []

for i in range(len(first_step)):
    oneway = []
    ind_row = first_step[i][0]
    ind_col = first_step[i][1]
    oneway.append(first_step[i])
    way(ind_row, ind_col)
    if len(res) == 3:
        a, b = [], []
        a.clear()
        b.clear()
        a = oneway.copy()
        b = oneway.copy()
        oneway.append(res[0])
        a.append(res[1])
        b.append(res[2])
        all_ways.append(a)
        all_ways.append(b)
        print('one', oneway)
        print('a', a)
        print('b', b)
    elif len(res) == 2:
        a = []
        a = oneway.copy()
        print('a', a)
        oneway.append(res[0])
        print('onew', oneway)
        a.append(res[1])
        print('a ext', a)
        all_ways.append(a)
        all_ways.append(oneway)
    if len(res) == 1:
        oneway.append(res[0])
        all_ways.append(oneway)
    print('one', oneway)
    print('alllall', all_ways)


# print('first ways', *result, sep = '\n')
print('one', oneway)
print('all', *all_ways, sep = '\n')