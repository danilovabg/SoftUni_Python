import re
patterm = re.compile(r"%(?P<name>[A-Z][a-z]+)%<(?P<product>[A-Z][a-z]+)>\|(?P<quant>[0-9]+)\|(?P<price>[0-9]+\.[0-9]*)")
operation = input()
total_income = 0
while operation != 'end of shift':
    s = 0
    res = re.finditer(patterm, operation)
    for el in res:
        s = float(el["quant"])*float(el["price"])
        total_income += s
        print(el["name"],": ", el["product"], " - ", f"{s:.2f}", sep='')
    operation = input()
print(f'Total income: {total_income:.2f}')
