population = list(map(int, input().split(', ')))
wealth = int(input())
no_money = False
while min(population) < wealth:
    if max(population) <= wealth:
        print('No equal distribution possible')
        no_money = True
        break
    w = wealth
    a_max = max(population)
    ind_max = population.index(a_max)
    ind_min = population.index(min(population))
    a_max -= (w-min(population))
    population[ind_min] = wealth
    population[ind_max] = a_max
if no_money == False:
    print(population)