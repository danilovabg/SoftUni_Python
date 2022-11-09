drinks = {'kid':'toddy','teens':'coke', 'young adults':'beer', 'adults':'whisky'}
age = int(input())
if age <= 14:
    a = 'kid'
elif 14 < age <= 18:
    a = 'teens'
elif 18 < age <= 21:
    a = 'young adults'
elif 21 < age:
    a = 'adults'
print(f'drink {drinks.get(a)}')