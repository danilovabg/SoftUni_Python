string = list(map(int, input().split(', ')))
if max(string)%10 == 0:
    n = max(string)/10
else:
    n = 1 + max(string)//10
z = 0
while z < n:
    print(f"Group of {z+1}0's: {list(filter(lambda x: (z+1)*10 >= x > z*10, string))}")
    z += 1