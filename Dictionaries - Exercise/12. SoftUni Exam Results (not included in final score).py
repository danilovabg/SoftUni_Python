exam_dict = {}
ban = []
line = input()
while line != 'exam finished':
    added = False
    elements = line.split('-')
    if len(elements) == 3:
        name = elements[0]
        if name not in ban:
            language = elements[1]
            score = elements[2]
            if language not in exam_dict:
                exam_dict[language] = [{name: [int(score)]}]
            elif language in exam_dict:
                course_student = exam_dict[language]
                for ind, val in enumerate(course_student):
                    if name in val:
                        val[name].append(int(score))
                        added = True
                if added is False:
                    exam_dict[language].append({name : [int(score)]})
    elif len(elements) == 2:
        name = elements[0]
        ban.append(name)
    line = input()


print('Results:')
for lang, st_list in exam_dict.items():
    for el in st_list:
        for n, sc in el.items():
            if n not in ban:
                print(f'{n} | {max(sc)}')
print('Submissions:')
for lang, st_list in exam_dict.items():
    quant = 0
    for el in st_list:
        for n, sc in el.items():
            quant += len(sc)
    print(f"{lang} - {quant}")
