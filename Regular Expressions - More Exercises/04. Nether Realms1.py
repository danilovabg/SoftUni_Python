import re
string = input()

string = re.sub(' ', '', string)
string = string.split(',')
pattern_health = r"([^0-9+-/*.])"
patterm_danage = r"-*[0-9.]*"
pattern_mult_divide = r"[//\*]"
dragons = {}
for el in string:
    health = 0
    damage = 0
    res = re.findall(pattern_health, el)
    res_damage = re.findall(patterm_danage, el)
    res_mult = re.findall(pattern_mult_divide, el)

    for num in res_damage:
        if num != '':
            damage += float(num)
    # print(res_mult)
    for element in res_mult:
        # print(damage)
        if element == '/':
            damage /= 2
        elif element == '*':
            damage *= 2
        # print(damage)
    for sym in res:
        health += ord(sym)
    dragons[el] = [health, damage]
sorted_dragons = sorted(dragons.items())
# print(sorted_dragons)
for dragon in sorted_dragons:
    print(f"{dragon[0]} - {dragon[1][0]} health, {dragon[1][1]:.2f} damage")

