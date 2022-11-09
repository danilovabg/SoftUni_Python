n = int(input())
num_list = []
filterred = []
for i in range(n):
    num = int(input())
    num_list.append(num)
command = input()
if command == 'even':
    for number in num_list:
        if number % 2 == 0:
            filterred.append(number)
elif command == 'odd':
    for number in num_list:
        if number % 2 == 1:
            filterred.append(number)
elif command == 'negative':
    for number in num_list:
        if number < 0:
            filterred.append(number)
elif command == 'positive':
    for number in num_list:
        if number >= 0:
            filterred.append(number)
print(filterred)