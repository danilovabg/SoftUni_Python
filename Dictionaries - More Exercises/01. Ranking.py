contest = input()
contest_dict = {}
while contest != 'end of contests':
    c = contest.split(":")
    if len(c) == 2:
        cont_name = c[0]
        password = c[1]
        if '=' not in cont_name and '=' not in password and '>' not in cont_name and '>' not in password:
            contest_dict[cont_name] = password
    contest = input()

submission = input()
submission_dict = {}
while submission != "end of submissions":
    s = submission.split('=>')
    cont_name = s[0]
    passw = s[1]
    name = s[2]
    score = int(s[3])
    if cont_name in contest_dict and passw == contest_dict[cont_name]:
        if name not in submission_dict:
            submission_dict[name] = {cont_name: score}
        elif name in submission_dict:
            if cont_name in submission_dict[name]:
                if score > submission_dict[name][cont_name]:
                    submission_dict[name][cont_name] = score
            else:
                submission_dict[name][cont_name] = score

    submission = input()
# print(submission_dict)
max_point = 0
for a, b in submission_dict.items():
    if sum(b.values()) > max_point:
        max_point = sum(b.values())

for r, t in submission_dict.items():
    if sum(t.values()) == max_point:
        candidat_name = r
        print(f"Best candidate is {candidat_name} with total {max_point} points.")
        print('Ranking:')

name_list = list(submission_dict.keys())
sorted_names = sorted(name_list)

for name in sorted_names:
    printed_course = []
    print(name)
    m = sorted(submission_dict[name].values(), reverse=True)
    # print('m', m)
    for el in m:
        for course, score in submission_dict[name].items():
            if score == el:
                if course not in printed_course:
                    printed_course.append(course)
                    print(f"#  {course} -> {score}")
