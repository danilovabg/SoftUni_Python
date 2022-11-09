num = float(input())
if num == 0:
    print('zero')
elif num < 0 and abs(num) < 1:
    print('small negative')
elif num > 0 and abs(num) < 1:
    print('small positive')
elif num < 0 and 1000000 >= abs(num) > 1:
    print('negative')
elif num > 0 and 1 <= num <= 1000000:
    print('positive')
elif num > 1000000:
    print('large positive')
elif num < 0 and abs(num) > 1000000:
    print('large negative')