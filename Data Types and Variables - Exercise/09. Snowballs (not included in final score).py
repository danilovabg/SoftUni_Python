n = int(input())
score = 0
max_score = 0
max_list =[]
for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    score = (weight/time)**quality
    if score > max_score:
        max_score = score
        max_list.clear()
        max_list.append(weight)
        max_list.append(time)
        max_list.append(quality)
print(f'{max_list[0]} : {max_list[1]} = {max_score:.0f} ({max_list[2]})')
