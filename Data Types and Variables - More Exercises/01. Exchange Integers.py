a = int(input())
b = input()
print('Before:')
print(f'a = {a}')
print(f'b = {b}')
temp = a
a = b
b = temp
print('After:')
print(f'a = {a}')
print(f'b = {b}')