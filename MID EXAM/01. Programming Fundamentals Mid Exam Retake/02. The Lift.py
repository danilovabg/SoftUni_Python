waiting_people = int(input())
lift = list(map(int, input().split()))
Done = False
for index, el in enumerate(lift):
    can_move = (4 - el)
    if waiting_people >= can_move:
        waiting_people -= can_move
        lift[index] = 4
    elif waiting_people < can_move:
        lift[index] = (waiting_people + el)
        waiting_people = 0
    if waiting_people == 0:
        Done = True
        break

if Done and sum(lift) < len(lift)*4:
    print('The lift has empty spots!')
elif Done is False:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
print(*lift)



