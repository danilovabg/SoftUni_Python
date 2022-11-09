prod = input()
quant = int(input())
def price(quant, prod):
    result = None
    if prod == 'coffee':
        result = quant*1.50
    elif prod == 'coke':
        result = quant*1.40
    elif prod == 'water':
        result = int(quant)*1.00
    elif prod == 'snacks':
        result = quant*2.00
    return result
print(f'{price(quant, prod):.2f}')