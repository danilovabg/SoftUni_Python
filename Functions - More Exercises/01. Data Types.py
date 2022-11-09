ty = input()
stri = input()
def funk(ty, str):
    if ty == 'int':
        res = int(stri)*2
    elif ty == 'real':
        res = f'{float(stri)*1.5:.2f}'
    elif ty == 'string':
        res = '$' + stri + '$'
    return res
print(funk(ty, str))