import re
string = input()
pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
res = re.findall(pattern, string)
for date in res:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")