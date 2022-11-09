lost_fights_count = int(input())
helmet_price = float(input())
sward_price = float(input())
shield_price = float(input())
armor_price = float(input())
summ = 0
shield_broke = 0
for i in range(1, lost_fights_count+1):
    if i % 2 == 0:
        summ += helmet_price
    if i % 3 == 0:
        summ += sward_price
    if i % 6 == 0:
        summ += shield_price
        shield_broke += 1
    if shield_broke % 2 == 0 and shield_broke > 0:
        summ += armor_price
        shield_broke = 0
print(f'Gladiator expenses: {summ:.2f} aureus')
