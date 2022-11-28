import re
string = input()
pattern = r"=([A-Z]{1}[A-Za-z]{2,})=|\/([A-Z]{1}[A-Za-z]{2,})\/"
res = re.findall(pattern, string)

dest = [el for tup in res for el in tup if el != '']
print('Destinations:', ', '.join(dest))
points = sum([len(x) for x in dest])
print(f'Travel Points: {points}')
