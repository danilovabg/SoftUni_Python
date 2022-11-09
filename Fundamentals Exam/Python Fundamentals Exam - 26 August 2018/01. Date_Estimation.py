from datetime import datetime

today = datetime(2018, 8, 25)

exam = list(map(int, input().split('-')))
exam[1] = str(exam[1])
if exam[1][0] == 0:
    exam[1] = str(exam[1][1:])
exam[1] = int(exam[1])
exam_date = datetime(exam[0], exam[1], exam[2])

delta = (exam_date - today)
x = int(delta.days)
if x > 0 and x != 1:
    print(delta.days, 'days left')
elif x == 1:
    print('Today date')
else:
    print('Passed')




