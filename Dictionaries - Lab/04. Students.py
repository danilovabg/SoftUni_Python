line = input()
students = {}
while ':' in line:
    element = line.split(':')
    students[element[0]] = [element[1], element[2]]
    line = input()
    if ':' not in line:
        if '_' in line:
            course = line.replace("_", " ")
        else:
            course = line

for key, value in students.items():
    if course in value:
        print(f"{key} - {value[0]}")
