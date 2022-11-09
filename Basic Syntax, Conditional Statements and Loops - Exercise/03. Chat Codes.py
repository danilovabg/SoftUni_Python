num = int(input())
while num > 0:
    n = int(input())
    if n == 88 :
        print('Hello')
    elif n == 86:
        print('How are you?')
    elif n < 88 and n != 86:
        print("GREAT!")
    else:
        print("Bye.")
    num -= 1