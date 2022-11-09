text = input()
letter_dict = {}
for letter in text:
    if letter != ' ' and letter not in letter_dict:
        letter_dict[letter] = 1
    elif letter != ' ' and letter in letter_dict:
        letter_dict[letter] += 1
[print(f"{l} -> {c}") for l, c in letter_dict.items()]