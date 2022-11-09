num = int(input())
stud_dic = {}
while num > 0:
    student = input()
    grade = float(input())
    if student not in stud_dic:
        stud_dic[student] = [grade]
    else:
        stud_dic[student].append(grade)
    num -= 1
final_dict = {}
for s, g in stud_dic.items():
    if sum(g)/len(g) >= 4.5:
        final_dict[s] = sum(g)/len(g)

[print(f"{s} -> {g:.2f}") for s, g in final_dict.items()]