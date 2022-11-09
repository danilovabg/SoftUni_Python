import re
string = input()
regex = r'\b[A-Z]{1}[a-z]{1,40}\b\s\b[A-Z]{1}[a-z]{1,40}\b'
matches = re.findall(regex, string)
print(' '.join(matches))
