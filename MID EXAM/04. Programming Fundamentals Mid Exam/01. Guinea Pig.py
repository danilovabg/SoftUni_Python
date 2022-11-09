food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
pig_kg = float(input())
day = 0
while day != 30:
    food_kg -= 0.3
    day += 1
    if day % 2 == 0:
        hay_kg -= food_kg * 0.05
    if day % 3 == 0:
        cover_kg -= pig_kg/3

if food_kg > 0 and hay_kg > 0 and cover_kg > 0:
    print(f'Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.')
else:
    print('Merry must go to the pet store!')