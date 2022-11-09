target = list(map(int, input().split()))

command = input()

while command != 'End':
    comm, id, val = command.split()
    id, val = int(id), int(val)
    if comm == 'Shoot' and 0 <= id < len(target):
        if (target[id] - val) > 0:
            target[id] = target[id] - val
        else:
            target.pop(id)
    if comm == 'Add':
        if 0 <= id < len(target):
            target.insert(id, val)
        else:
            print('Invalid placement!')
    if comm == 'Strike':
        i1 = id - val
        i2 = id + val
        if 0 <= i1 < len(target) and 0 <= i2 < len(target):
            target = target[: i1] + target[i2+1:]
        else:
            print('Strike missed!')
    command = input()

target = [str(x) for x in target]
if command == 'End':
    print('|'.join(target))
