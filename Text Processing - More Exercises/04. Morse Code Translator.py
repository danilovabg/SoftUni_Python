morze_list = input().split(' | ')
letters = []
normal_words = ''

morze = { '.-': 'a', '-..': 'b', '-.-.': 'c', '-..': 'd', '.': 'e' , '..-.': 'f', '--.': 'g', '....': 'h',
         '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
         '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v',  '.--': 'w',
         '-..-': 'x', '-.--': 'y', '--..': 'z'}
for word in morze_list:
    w = word.split()
    letters.append(w)
for el in letters:
    for sym in el:
        normal_words += morze[sym].upper()

    normal_words += ' '

print(normal_words)