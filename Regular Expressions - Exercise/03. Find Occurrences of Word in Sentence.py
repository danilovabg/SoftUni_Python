import re
line = input().lower()
pat = input().lower()
pattern = r'(\b)'+pat+r'(\b)'
res = re.findall(pattern, line)

print(len(res))
