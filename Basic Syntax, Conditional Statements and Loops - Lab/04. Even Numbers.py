n = int(input())
while n > 0:
    num = int(input())
    if num % 2 == 1:
        print(f'{num} is odd!')
        break
    n -=1
if n == 0:
    print('All numbers are even.')