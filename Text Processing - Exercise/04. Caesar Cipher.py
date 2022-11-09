string = input()
new_string = ''
for sym in string:
    new_string += chr(ord(sym)+3)
print(new_string)