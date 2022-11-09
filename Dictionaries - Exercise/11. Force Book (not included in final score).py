sides_dict = {}
user = input()
user_list = []
while user != 'Lumpawaroo':
    for s, n in sides_dict.items():
        user_list.extend(n)
    if ' | ' in user:
        u = user.split(' | ')
        side, name = u[0], u[1]
        if side not in sides_dict and name not in user_list:
            sides_dict[side] = [name]
        elif side in sides_dict and name not in user_list:
            sides_dict[side].append(name)
    elif ' -> ' in user:
        u = user.split(' -> ')
        name, side = u[0], u[1]
        if name not in user_list and side in sides_dict:
            sides_dict[side].append(name)
        elif name in user_list:
            if side in sides_dict and name in sides_dict[side]:
                pass
            else:
                for q, w in sides_dict.items():
                    if name in w:
                        sides_dict[q].remove(name)
                if side in sides_dict:
                    sides_dict[side].append(name)
                else:
                    sides_dict[side] = [name]
        elif name not in user_list and side not in sides_dict:
            sides_dict[side] = [name]
        print(f'{name} joins the {side} side!')

    user = input()

for si_de, na_me in sides_dict.items():
    if len(na_me) != 0:
        print(f'Side: {si_de}, Members: {len(na_me)}')
        [print(f'! {el}') for el in na_me]
