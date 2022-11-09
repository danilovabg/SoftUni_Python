items = input().split(', ')

command = input()

while command != 'Craft!':
    comm, item = command.split(' - ')
    if comm == 'Collect' and item not in items:
        items.append(item)
    elif comm == "Drop" and item in items:
        items.remove(item)
    elif comm == 'Combine Items':
        old, new = item.split(':')
        if old in items:
            id = items.index(old) + 1
            items.insert(id, new)
    elif comm == 'Renew' and item in items:
        items.remove(item)
        items.append(item)
    command = input()

print(', '.join(items))
