v = False
name = input()
while name != 'Welcome!':
    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6 and name != 'Voldemort':
        print(f'{name} goes to Hufflepuff.')
    elif name == 'Voldemort':
        print('You must not speak of that name!')
        v = True
        break
    name = input()
    if v:
        break
if v:
    pass
else:
    print('Welcome to Hogwarts.')