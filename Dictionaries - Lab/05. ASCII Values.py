letters = input().split(', ')
letter_dict = {}
for l in letters:
    letter_dict[l] = ord(l)

print(letter_dict)