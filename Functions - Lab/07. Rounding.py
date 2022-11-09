string = input().split(' ')
def rounring(string):
    for i in range(len(string)):
        string[i] = float(string[i])
        string[i] = round(string[i])
    return string
print(rounring(string))
