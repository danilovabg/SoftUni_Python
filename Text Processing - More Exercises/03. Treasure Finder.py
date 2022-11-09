keys = list(map(int, input().split()))
line = input()
new_el = ''
new_list = []
while line != 'find':
    new_el = ''
    ind = 0
    for el in line:
        if ind == len(keys):
            ind = 0
        new_el += chr(ord(el) - keys[ind])
        ind += 1
    treasure, coordinate = '', ''
    start_treasure = False
    start_coocdinate = False
    for el in new_el:
        if start_treasure and el != '&':
            treasure += el
        elif start_treasure and el == '&':
            break
        if el == '&':
            start_treasure = True

    for el in new_el:
        if start_coocdinate and el != '>':
            coordinate += el
        elif start_coocdinate and el == '>':
            break
        if el == '<':
            start_coocdinate = True

    print(f"Found {treasure} at {coordinate}")
    line = input()