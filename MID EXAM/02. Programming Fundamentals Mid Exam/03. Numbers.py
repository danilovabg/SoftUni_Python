read = list(map(int, input().split()))

numbers_greater_then_avg = list(filter(lambda x: x > sum(read)/len(read), read))
numbers_greater_then_avg.sort(reverse=True)
if len(numbers_greater_then_avg) > 5:
    print(*numbers_greater_then_avg[:5])
else:
    print(*numbers_greater_then_avg)
if len(numbers_greater_then_avg) == 0:
    print('No')