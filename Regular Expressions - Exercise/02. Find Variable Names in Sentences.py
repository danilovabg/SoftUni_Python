import re
line = input()

pattern = r'(^|\b)_[A-Za-z]+($|\b)'
res = re.finditer(pattern, line)
nums = []
for el in res:
    nums.append(el.group()[1:])
print(*nums, sep=',')

