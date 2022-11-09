arr = list(map(int, input().split()))

command = input()

while command != 'end':
    comm = command.split()
    if comm[0] =='swap':
        id1, id2 = int(comm[1]), int(comm[2])
        arr[id1], arr[id2] = arr[id2], arr[id1]
    elif comm[0] == 'multiply':
        id1, id2 = int(comm[1]), int(comm[2])
        arr[id1] = arr[id1]* arr[id2]
    elif comm[0] == 'decrease':
        arr = [x-1 for x in arr]

    command = input()
arr = [str(x) for x in arr]
print(', '.join(arr))