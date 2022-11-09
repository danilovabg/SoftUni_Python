ban = input().split(', ')
text = input()
for el in ban:
    while el in text:
        text = text.replace(el, "*"*len(el))
print(text)