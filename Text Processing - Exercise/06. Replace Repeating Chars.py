string = input()
newstr = ' '
for sym in string:
    if sym != newstr[-1]:
        newstr += sym
print(newstr[1:])