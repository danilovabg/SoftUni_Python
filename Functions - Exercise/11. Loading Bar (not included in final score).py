num = int(input())//10
def load(num):
    if num < 10:
        z = str(num*10) + '% ' + '['+'%'*num + '.'*(10-num)+']'
        a = 'Still loading...'
    elif num == 10:
        z = '100% Complete!'
        a = '[%%%%%%%%%%]'
    return [z, a]
for el in load(num):
    print(el)
