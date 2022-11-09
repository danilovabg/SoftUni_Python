string = list(map(int, input().split(', ')))
even, odd, pos, neg = [], [], [], []
[even.append(x) for x in string if x%2 == 0]
[odd.append(x) for x in string if x%2 == 1]
[pos.append(x) for x in string if x >= 0]
[neg.append(x) for x in string if x < 0]
print('Positive: ', end='')
print(*pos, sep=', ')
print('Negative: ', end='')
print(*neg, sep=', ')
print('Even: ', end='')
print(*even, sep=', ')
print('Odd: ', end='')
print(*odd, sep=', ')