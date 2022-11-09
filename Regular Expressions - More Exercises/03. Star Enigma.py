import re
num = int(input())
pattern = re.compile(r"@(?P<planet>[A-Z][a-z]+)[^@\-!:>]*:\d+!(?P<attac>A|D)![^@\-!:>]*->\d+")
attaced = []
destruct = []
while num > 0:
    message = input()
    m = message.lower()
    summ_star = m.count('s')+m.count('t')+m.count('a')+m.count('r')
    decripted = ''
    for sym in message:
        decripted += chr(ord(sym)-summ_star)
    res = pattern.finditer(decripted)
    for el in res:
        if el["attac"] == 'A':
            attaced.append(el["planet"])
        elif el["attac"] == 'D':
            destruct.append(el["planet"])
    num -= 1

print(f"Attacked planets: {len(attaced)}")
if len(attaced) != 0:
    for el in sorted(attaced):
        print(f"-> {el}")
print(f"Destroyed planets: {len(destruct)}")
if len(destruct) != 0:
    for el in sorted(destruct):
        print(f"-> {el}")