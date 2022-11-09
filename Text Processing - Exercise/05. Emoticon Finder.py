string = input()
for ind in range(len(string)):
    if string[ind] == ':' and string[ind+1] != ' ' :
        print(string[ind]+string[ind+1])
