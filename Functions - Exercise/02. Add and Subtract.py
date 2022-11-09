a = int(input())
b = int(input())
c = int(input())
def sum_numbers(a, b):
    res = a + b
    return res
def subtract(c):
    r = sum_numbers(a, b) - c
    return r
print(subtract(c))