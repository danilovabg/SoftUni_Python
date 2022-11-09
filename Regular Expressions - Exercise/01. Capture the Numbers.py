import re
text = ""
while True:
    x = input()
    if x:
        text += x + " "
    else:
        break

pattern = r"\d+"
result = re.findall(pattern, text)
print(*result)
