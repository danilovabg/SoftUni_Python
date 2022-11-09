q_decor = int(input())
days_left = int(input())
q = 0 # amount of days passed
s = 0 # budget
spirit = 0
ts = 0
m = 0

if 100 < days_left < 1 or 100 < q_decor < 1:
    pass
else:
    while days_left > 0:
        set = False
        q += 1
        if q % 11 == 0:
            m += 2
        if q % 2 == 0:
            s += 2*(q_decor+m)
            spirit += 5
        if q % 3 == 0:
            s += (5 + 3)*(q_decor+m)
            spirit += 3 + 10
            set = True
        if q % 5 == 0:
            s += 15*(q_decor+m)
            spirit += 17
            if set:
                spirit += 30
        if q % 10 == 0:
            spirit -= 20
            s += (5 + 3 + 15)

        days_left -= 1
if q % 10 == 0:
    spirit -= 30

print(f'Total cost: {s}')
print(f'Total spirit: {spirit}')
