string = list(input())
num, other, take_list, skip_list, result = [], [], [], [], []
for i in string:
    try:
        num.append(int(i))
    except ValueError:
        other.append(i)
[take_list.append(num[x]) for x in range(len(num)) if x % 2 == 0]
[skip_list.append(num[x]) for x in range(len(num)) if x % 2 != 0]
sn = sum(num)
while sn > 0:
    for i in range(len(take_list)):
        result.extend(other[:take_list[i]])
        x = take_list[i]+skip_list[i]
        other = other[x:]
        sn -= (skip_list[i] + take_list[i])
print("".join(result))