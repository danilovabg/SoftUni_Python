key = int(input())
n = int(input())
for i in range(n):
    simbol = input()
    print(chr(ord(simbol)+key), end ='')