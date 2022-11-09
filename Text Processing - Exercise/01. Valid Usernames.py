usernames = input().split(", ")
valid = []

for el in usernames:
    expected_symbols = False
    c = 0
    for sym in el:
        if ord(sym) in range(65, 91) or ord(sym) in range(97, 123) or sym == '-' or sym == '_' or ord(sym) in range(48, 58):
            c += 1
    if c == len(el):
        expected_symbols = True
    if 3 <= len(el) <= 16 and expected_symbols is True:
        valid.append(el)
print(*valid, sep='\n')

