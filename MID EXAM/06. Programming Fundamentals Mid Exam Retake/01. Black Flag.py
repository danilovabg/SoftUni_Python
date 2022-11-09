days, plunder, expected = int(input()), int(input()), float(input())
summ = 0

if days != 0 and plunder != 0:
    for day in range(1, days+1):
        if day % 3 == 0 and day % 5 != 0:
            summ += 1.5*plunder
        elif day % 5 == 0 and day % 3 != 0:
            summ += plunder
            summ *= 0.7
        elif day % 15 == 0:
            summ += 1.5 * plunder
            summ *= 0.7
        else:
            summ += plunder
if summ >= expected:
    print(f'Ahoy! {summ:.2f} plunder gained.')
else:
    print(f'Collected only {100*summ/expected:.2f}% of the plunder.')
