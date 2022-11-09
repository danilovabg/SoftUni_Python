a_list = {'A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11'}
b_list = {'B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11'}
#referi = set(input().split(' '))
#print(f'Team A - {len(a_set.difference(referi))}; Team B - {len(b_set.difference(referi))}')
#if len(a_set.difference(referi)) < 7 or len(b_set.difference(referi)) < 7:
 #   print('Game was terminated')

referi = input()
referi = referi.split(' ')
br = False
for j in referi:
    if j in a_list:
        a_list.remove(j)
        if len(a_list) < 7:
            br = True
            break
    elif j in b_list:
        b_list.remove(j)
        if len(b_list) < 7:
            br = True
            break
print(f'Team A - {len(a_list)}; Team B - {len(b_list)}')
if br:
    print('Game was terminated')
