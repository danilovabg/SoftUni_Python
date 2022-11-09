n = int(input())
Fal = False
for i in range(2, n):
    if n % i == 0:
        print(False)
        Fal = True
        break
    if Fal:
        break
if Fal is False:
    print(True)