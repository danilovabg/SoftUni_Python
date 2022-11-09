energy = int(input())
distance = input()
win = 0

while distance != 'End of battle':

    if int(distance) <= energy:
        win += 1
        energy -= int(distance)
        if win % 3 == 0:
            energy += win
    else:
        print(f'Not enough energy! Game ends with {win} won battles and {energy} energy')
        break
    distance = input()

if distance == 'End of battle':
    print(f'Won battles: {win}. Energy left: {energy}')
