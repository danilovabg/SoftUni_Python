import re
string = input()

pattern = r"(?::{2}[A-Z]{1}[a-z]{2,}:{2})|(?:\*\*[A-Z]{1}[a-z]{2,}\*\*)"
res = re.findall(pattern, string)

coolnest = [int(x) for x in string if x.isdigit()]
mul = lambda coolnest: coolnest[0] * mul(coolnest[1:]) if coolnest else 1
total_coolnest = mul(coolnest)
print(f'Cool threshold: {total_coolnest}')
print(f'{len(res)} emojis found in the text. The cool ones are:')
cool_emoji = lambda el: ord(el[0])+cool_emoji(el[1:]) if el else 0

[print(word) for word in res if cool_emoji(word[2:-2]) > total_coolnest]
