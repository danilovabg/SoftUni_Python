line1 = input()
line2 = input()
while line1 in line2:
    line2 = line2.replace(line1, '')

print(line2)
