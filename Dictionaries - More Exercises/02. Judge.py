contest = input()
person_dict = {}
exam_dict = {}
aded_list = []

while contest != 'no more time':
    c = contest.split(' -> ')
    name = c[0]
    exercise = c[1]
    points = int(c[2])
    if exercise not in aded_list:
        aded_list.append(exercise)
    if name not in person_dict:
        person_dict[name] = 0
    if exercise not in exam_dict:
        exam_dict[exercise] = {name: points}
        person_dict[name] += points
    else:
        if name in exam_dict[exercise]:
            if points > exam_dict[exercise][name]:
                person_dict[name] -= exam_dict[exercise][name]
                person_dict[name] += points
                exam_dict[exercise][name] = points
        else:
            exam_dict[exercise][name] = points
            person_dict[name] += points

    contest = input()
# print(person_dict)
# print(exam_dict)

for ex in aded_list:
    new_list = []
    for contest, participents in exam_dict.items():
        if contest == ex:
            print(f"{contest}: {len(participents)} participants")
            num = 1
            for name, score in participents.items():
                new_list.append((name, score))
            new_list.sort(key=lambda x: (-x[1], x[0]))
            for ind in range(len(new_list)):
                print(f"{num}. {new_list[ind][0]} <::> {new_list[ind][1]}")
                num += 1

print('Individual standings:')
new_person_list = []
for name, score in person_dict.items():
    new_person_list.append((name, score))

new_person_list.sort(key=lambda x: (-x[1], x[0]))
# print(new_person_list)
for ind in range(1, len(new_person_list)+1):
    print(f"{ind}. {new_person_list[ind-1][0]} -> {new_person_list[ind-1][1]}")