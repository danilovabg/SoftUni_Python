import math
import re
string = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
match = re.finditer(pattern, string)
# print(match)
for el in match:
    print(el.group(), end=' ')