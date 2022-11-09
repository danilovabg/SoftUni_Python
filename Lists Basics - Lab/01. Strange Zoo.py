tail = input()
body = input()
head= input()
meercat = [tail, body, head]
meercat[0], meercat[2] = meercat[2], meercat[0]
print(meercat)