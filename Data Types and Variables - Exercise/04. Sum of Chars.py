n = int(input())
s = 0
if n <= 20:
    while n > 0:
        a = input()
        s += ord(a)
        n -= 1
    print(f'The sum equals: {s}')
