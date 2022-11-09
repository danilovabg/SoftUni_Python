import math
centuries = int(input())
days =math.floor(centuries*100*365.2422)
print(f'{centuries} centuries = {centuries*100} years = {days:.0f} days = {days*24:.0f} hours = {days*24*60:.0f} minutes')