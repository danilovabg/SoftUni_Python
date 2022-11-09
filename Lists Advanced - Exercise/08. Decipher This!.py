string = list(map(list, input().split()))
for word in string:
    z = 0
    j = 0
    for i in word:
        try:
            z = z*10 + int(i)
            word.remove(i)
            word.insert(0, chr(z))
            j += 1
        except ValueError:
            break
    while j > 1:
        word.pop(j-1)
        j -= 1
    word[1], word[len(word) - 1] = word[len(word) - 1], word[1]
for w in string:
    print(*w, sep='', end=' ')