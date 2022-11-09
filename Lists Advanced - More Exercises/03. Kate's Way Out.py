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
            pass#
# print(*lab, sep='\n')
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
all_ways = []
for step in result:
    all_ways.append([step])
cheked = []
dedend = []
final_checked = []
def lab_funk(all_ways):
    dedend = []
    count = 0
    cheked = []
    for i in range(len(all_ways)):
        if all_ways[i] not in cheked:
            cheked.append(all_ways[i])
            ind_row = all_ways[i][-1][0]
            ind_col = all_ways[i][-1][1]
            way(ind_row, ind_col)
            if len(all_ways[i]) > 1 and len(res) > 0:
                res.remove(all_ways[i][-2])
            if len(res) == 0:
                if all_ways[i][-1][0] != 0 and all_ways[i][-1][0] != len(lab)-1 and all_ways[i][-1][1] != 0 and all_ways[i][-1][1] != len(lab[0])-1:
                    dedend.append(all_ways[i])
                else:
                    x = all_ways[i].copy()
                    cheked.append(x)
                    final_checked.append(all_ways[i])
                    print('cheked', cheked)
            else:
                count += 1
                if len(res) == 3:
                                a, b = [], []
                                a = all_ways[i].copy()
                                b = all_ways[i].copy()
                                if res[0] not in all_ways[i]:
                                    all_ways[i].append(res[0])
                                if res[1] not in all_ways[i]:
                                    a.append(res[1])
                                if res[2] not in all_ways[i]:
                                    b.append(res[2])
                                if a not in all_ways[i]:
                                    all_ways.append(a)
                                if b not in all_ways[i]:
                                    all_ways.append(b)
                elif len(res) == 2:
                                a = []
                                a = all_ways[i].copy()
                                if res[0] not in all_ways[i]:
                                    all_ways[i].append(res[0])
                                if res[1] not in all_ways[i]:
                                    a.append(res[1])
                                if a not in all_ways:
                                    all_ways.append(a)
                elif len(res) == 1:
                    if res[0] not in all_ways[i]:
                        all_ways[i].append(res[0])
    print('66666677777777777777777777')
    print('all', *all_ways, sep='\n')
    for c in cheked:
        final_checked.append(c)
        all_ways.remove(c)
    print(final_checked)
    for d in dedend:
        all_ways.remove(d)
    if count != 0:
        lab_funk(all_ways)
        print('one more time')
        print()
    print('finaly end')
    return 1


lab_funk(all_ways)
end = []
for i in all_ways:
    if i[-1][0] == 0 or i[-1][0] == len(lab)-1 or i[-1][1] == 0 or i[-1][1] == len(lab[0])-1:
        end.append(i)
if len(end) == 0:
    print('Kate cannot get out')
else:
    max_steps = []
    for j in end:
        if len(j) > len(max_steps):
            max_steps = j
    print(f'Kate got out in {len(max_steps)+1} moves')
# print(*all_ways, sep = '\n')
