num = int(input())
reguster_dict = {}
while num > 0:
    user = input().split()
    if user[0] == 'register' and user[1] not in reguster_dict:
        reguster_dict[user[1]] = user[2]
        print(f'{user[1]} registered {user[2]} successfully')
    elif user[0] == 'register' and user[1] in reguster_dict:
        print(f'ERROR: already registered with plate number {reguster_dict[user[1]]}')
    elif user[0] == 'unregister' and user[1] in reguster_dict:
        print(f"{user[1]} unregistered successfully")
        reguster_dict.pop(user[1])
    elif user[0] == 'unregister' and user[0] not in reguster_dict:
        print(f'ERROR: user {user[1]} not found')
    num -= 1

[print(f"{name} => {car}") for name, car in reguster_dict.items()]
