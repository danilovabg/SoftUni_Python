import re
text = input()

title = r"<title>(?P<te>.+)</title>.+"
body = r"<body>(?P<cont>.+)+</body>"
title_from_text = re.findall(title, text)

content = r">([^<>]+)<"
content_of_text = re.findall(content, text)

line = ''
for el in content_of_text:
    if el != title_from_text[0] and el != '\\n':
        line += el + ' '
conten = line.split('\\n')
content = ''
for el in conten:
    content += el
clean_content = re.sub("\s+", ' ', content)
print(f"Title: {title_from_text[0]}")
print(f'Content: {clean_content}')
