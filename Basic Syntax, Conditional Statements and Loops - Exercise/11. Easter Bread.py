buget = float(input())
flo = float(input())
one =flo + flo*1.25*0.25 + 0.75*flo
q = 0
egs = 0
while buget > 0:
    if buget < one:
        break
    buget -= one
    q += 1
    egs += 3
    if q % 3 == 0:
        egs -=(q-2)

print(f'You made {q} loaves of Easter bread! Now you have {egs} eggs and {buget:.2f}BGN left.')
