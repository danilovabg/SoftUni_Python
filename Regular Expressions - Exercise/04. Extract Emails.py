import re
text = input()
pattern = r"((^|\s)[A-Za-z0-9]{1}[A-Za-z-_.0-9]+@[A-Za-z]+[-]*[A-Za-z]+\.[A-Za-z]{2,}(\.[A-Za-z]{2,})?\b)"
res = re.findall(pattern, text)
for el in res:
    print(el[0])