string = input()
letters = []
nums = []
other = []
for letter in string:
    if ord(letter) in range(65, 91) or ord(letter) in range(97, 123):
        letters.append(letter)
    elif ord(letter) in range(48, 58):
        nums.append(letter)
    else:
        other.append(letter)

print(*nums, sep='')
print(*letters, sep='')
print(*other, sep = '')