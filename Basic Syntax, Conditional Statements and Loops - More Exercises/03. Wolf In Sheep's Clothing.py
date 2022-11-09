string = input()
string.split(', ')
word_list = string.split(', ', -1)
word_list.reverse()
if word_list[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    i = word_list.index('wolf')
    print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
