num_data = float(input())
def grade(num):
    if 2.00 <= num <= 2.99:
        return 'Fail'
    elif 3.00 <= num <= 3.49:
        return 'Poor'
    elif 3.50 <= num <= 4.49:
        return 'Good'
    elif 4.50 <= num <= 5.49:
        return 'Very Good'
    elif 5.50 <= num <= 6.00:
        return 'Excellent'
print(grade(num_data))