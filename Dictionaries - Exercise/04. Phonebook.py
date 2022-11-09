phone = input()
phonebook = {}
while '-' in phone:
    people = phone.split('-')
    phonebook[people[0]] = people[1]
    phone = input()

num = int(phone)
while num > 0:
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f'Contact {name} does not exist.')
    num -= 1