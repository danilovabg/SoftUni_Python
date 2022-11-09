stri = list(input())
def summ(stri):
    even = []
    odd = []
    for i in range(len(stri)):
        stri[i] = int(stri[i])
        if stri[i] % 2 == 0:
            even.append(stri[i])
        elif stri[i] % 2 == 1:
            odd.append(stri[i])
    s_even = sum(even)
    s_odd = sum(odd)
    return [s_even, s_odd]
print(f'Odd sum = {summ(stri)[1]}, Even sum = {summ(stri)[0]}')
