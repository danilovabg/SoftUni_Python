num = int(input())
synonim_dict = {}
while num > 0:
    word = input()
    synon = input()
    if word not in synonim_dict:
        synonim_dict[word] = [synon]
    else:
        synonim_dict[word].append(synon)
    num -= 1

for w, s in synonim_dict.items():
    print(w, end=' - ')
    print(*s, sep=', ')