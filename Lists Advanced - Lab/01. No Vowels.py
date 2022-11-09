string = list(input())
vow = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
def vowels(string):
    new_string = []
    for el in range(len(string)):
        if string[el] not in vow:
            new_string.append(string[el])
    return new_string
print(*vowels(string), sep='')