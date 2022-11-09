courses = {}

student = input()
while student != 'end':
    st = student.split(' : ')
    if st[0] in courses:
        courses[st[0]].append(st[1])
    else:
        courses[st[0]] = [st[1]]
    student = input()

for name in courses:
    print(f"{name}: {len(courses[name])}", end='\n-- ')
    print(*courses[name], sep='\n-- ')