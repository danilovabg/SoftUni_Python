let1 = input()
let2 = input()
string = input()
sum = 0
for el in string:
    if ord(el) in range(ord(let1)+1, ord(let2)):
        sum += ord(el)
print(sum)