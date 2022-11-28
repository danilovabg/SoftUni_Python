import re
pattern = r"@#+([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})@#+"
n = int(input())

for str in range(n):
    string=input()
    res = re.findall(pattern, string)
    if len(res) > 0:
        num = ''
        for el in res[0]:
            if el.isdigit():
                num += el
        [print(f'Product group: {num}') if num != '' else print(f'Product group: 00')]
    else:
        print('Invalid barcode')