string = list(input())
counter = 0
s = ['s', 'S']
u = ['u', 'U']
n = ['n', 'N']
a = ['a', 'A']
d = ['d', 'D']
w = ['w', 'W']
t = ['t', 'T']
e = ['e', 'E']
r = ['r', 'R']
f = ['f', 'F']
ii = ['i', 'I']
h = ['h', 'H']
for i in range(len(string)):
    if len(string) >= 3:
        if string[i] in s and i <= (len(string)-3):
            if string[i+1] in u:
                if string[i+2] in n:
                    counter += 1
                    #print('sun')
    if len(string) >=4:
        if string[i] in s and i <= (len(string)-4):
            if string[i+1] in a:
                if string[i+2] in n:
                    if string[i+3] in d:
                        counter += 1
                        #print('sand')
    if len(string) >= 5:
        if string[i] in w and i <= (len(string)-5):
            if string[i+1] in a:
                if string[i+2] in t:
                    if string[i+3] in e:
                        if string[i+4] in r:
                            counter += 1
                            #print('water')
    if len(string) >= 4:
        if string[i] in f and i <= (len(string)-4):
            if string[i+1] in ii:
                if string[i+2] in s:
                    if string[i+3] in h:
                        counter += 1
                        #print('fish')
    else:
        pass
print(counter)
