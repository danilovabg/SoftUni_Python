import re

text = input()
pattern = r"(?:\|(?P<food>[A-Za-z\s]+)\|" \
          r"(?P<date>\d{2}\/\d{2}\/\d{2})\|" \
          r"(?P<calory>\d+)\|)|(?:#" \
          r"(?P<food1>[A-Za-z\s]+)#" \
          r"(?P<date1>\d{2}\/\d{2}\/\d{2})#" \
          r"(?P<calory1>\d+)#)"
res = re.findall(pattern, text)
result = [x for y in res for x in y if x != '']
ckal = [int(x) for x in result[2::3]]
print(f'You have food to last you for: {sum(ckal)//2000} days!')

for i in range(len(result)//3):
    print(f'Item: {result[3*i]}, Best before: {result[3*i+1]}, Nutrition: {result[3*i+2]}')
