string = input().split()
num = []
for el in string:
    n = 0
    if ' ' in el:
        el = el.replace(' ', '')
    if ord(el[0]) in range(65, 91):
        n += int(el[1:len(el)-1])/(ord(el[0])-64)
    if ord(el[0]) in range(97, 123):
        n += int(el[1:len(el)-1]) * (ord(el[0])-96)
    if ord(el[-1]) in range(65, 91):
        n -= (ord(el[-1]) - 64)
    if ord(el[-1]) in range(97, 123):
        n += (ord(el[-1]) - 96)
    num.append(n)
print(f"{sum(num):.2f}")
