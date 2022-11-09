heart = list(map(int, input().split('@')))
command = input()

id = 0
while command != 'Love!':
    jump, ind = command.split()
    id += int(ind)
    if id >= len(heart):
        id = 0
    #print(id)
    if heart[id] == 0:
        print(f"Place {id} already had Valentine's day.")
    else:
        heart[id] -= 2
        if heart[id] == 0:
            print(f"Place {id} has Valentine's day.")
    #print(heart)
    command = input()

if command == 'Love!':
    print(f"Cupid's last position was {id}.")
    if sum(heart) == 0:
        print('Mission was successful.')
    else:
        fail = [x for x in heart if x != 0]
        print(f"Cupid has failed {len(fail)} places.")