needed = float(input())
num_of_battless = int(input())
experience = int(input())
total_exp = 0
counter = 0
while total_exp < needed or num_of_battless > counter:
    counter += 1
    if counter % 3 == 0 and counter % 15 != 0 and counter % 5 != 0:
        total_exp += experience*1.15
    elif counter % 5 == 0 and counter % 3 != 0:
        total_exp += experience*0.9
    elif counter % 15 == 0:
        total_exp += experience*1.05
    else:
        total_exp += experience
    #print(total_exp)
    if total_exp >= needed:
        print(f'Player successfully collected his needed experience for {counter} battles.')
        break
    if num_of_battless <= counter:
        break
    experience = int(input())


if total_exp < needed:
    print(f'Player was not able to collect the needed experience, {needed-total_exp:.2f} more needed.')