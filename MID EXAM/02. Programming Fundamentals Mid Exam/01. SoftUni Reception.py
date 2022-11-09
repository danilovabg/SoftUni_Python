
first, second, third = int(input()), int(input()), int(input())
students = int(input())
st_per_hour = first + second + third
hour = 0
counter = 0
while students > 0:
    students -= st_per_hour
    hour += 1
    counter += 1
    if counter % 3 == 0 and students > 0:
        hour += 1
print(f'Time needed: {hour}h.')
