happ = list(map(int, input().split(' ')))
factor = int(input())
happyness = list(map(lambda x: x*factor, happ))

filt = list(filter(lambda x: x > sum(happyness)/len(happyness), happyness))
if len(filt) >= len(happyness)/2:
    print(f'Score: {len(filt)}/{len(happyness)}. Employees are happy!')
else:
    print(f'Score: {len(filt)}/{len(happyness)}. Employees are not happy!')