n = int(input())
notes = {}
for i in range(n):
    pieсe, composer, key = input().split('|')
    notes[pieсe] = [composer, key]

command = input()
while command != 'Stop':
    command = command.split('|')
    if command[0] == 'Add':
        if command[1] in notes:
            print(f"{command[1]} is already in the collection!")
        else:
            notes[command[1]] = [command[2], command[3]]
            print(f'{command[1]} by {command[2]} in {command[3]} added to the collection!')
    elif command[0] == 'Remove':
        if command[1] in notes:
            notes.pop(command[1])
            print(f'Successfully removed {command[1]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        if command[1] in notes:
            notes[command[1]][1] = command[2]
            print(f'Changed the key of {command[1]} to {command[2]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
    command = input()

for piece, info in notes.items():
    print(f'{piece} -> Composer: {info[0]}, Key: {info[1]}')