stud = dict()
num = int(input())
lectures = int(input())
bonus = int(input())

if num !=0 and lectures != 0 and bonus != 0:
    for n in range(num):
        st_att = int(input())
        bon = round(st_att/lectures * (5+bonus))
        stud[bon] = st_att
    print(f"Max Bonus: {max(stud)}.\nThe student has attended {stud[max(stud)]} lectures.")
else:
    print(f"Max Bonus: 0.\nThe student has attended {lectures} lectures.")


