import re
text = input()
info = False
while text != 'make migrations':
    regex_name ='name\s{1}is\s{1}([A-Z][a-z]+\s{1}[A-Z][a-z]+)'
    regex_age = '\s([0-9]+)\s'
    regex_birth = 'on\s{1}([0-9]{2}-[0-9]{2}-[0-9]{4})\.'
    name = re.findall(regex_name, text)
    age = re.findall(regex_age, text)
    birth = re.findall(regex_birth, text)

    if len(name) != 0 and len(age) != 0 and len(birth) != 0 and 9 < int(age[0]) < 100:
        print(f"Name of the person: {name[0]}.\n"
              f"Age of the person: {age[0]}.\n"
              f"Birthdate of the person: {birth[0]}.")
        info = True
    name, age, birth = [], [], []
    text = input()
if info is False:
    print('DB is empty')