num = int(input())
train = []
def train_fun(num):
    for n in range(num):
        train.append(0)
    command = input().split(' ')
    while command[0] != 'End':
        if command[0] == 'add':
            train[num-1] += int(command[1])
        elif command[0] == 'insert':
            train[int(command[1])] += int(command[2])
        elif command[0] == 'leave':
            i = command[1]
            train[int(command[1])] -= int(command[2])
        command = input().split()
    return train
print(train_fun(num))