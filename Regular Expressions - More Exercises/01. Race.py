import re
names = input().split(', ')
pattern = r"[A-Za-z]"
km = r'[1-9]'
race = input()
participants = {}
while race != 'end of race':
    name = ''
    run = 0
    res = re.findall(pattern, race)
    score = re.findall(km,race)
    for el in res:
        name += el
    if name in names:
        for el in score:
            run += int(el)
        if name in participants:
            participants[name] += run
        else:
            participants[name] = run
    race = input()

participants_sorted = sorted(participants.items(), key=lambda item: -item[1])
print(f"1st place: {participants_sorted[0][0]}")
print(f"2nd place: {participants_sorted[1][0]}")
print(f"3rd place: {participants_sorted[2][0]}")
