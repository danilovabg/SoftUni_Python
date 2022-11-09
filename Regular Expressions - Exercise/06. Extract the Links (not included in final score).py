import re
pattern = r"((www)\.([A-Za-z0-9-]+)(\.[a-z]+)+)"
text = ''
while True:
    string = input()
    if string:
        text += string +' '
    else:
        break
res = re.findall(pattern, text)
# print(*res, sep='\n')
for el in res:
    print(el[0])