pokemon = list(map(int,input().split()))
summ = 0
while len(pokemon) > 0:
    ind = int(input())
    if ind < 0:
        a = pokemon.pop(0)
        summ += a
        pokemon.insert(0, pokemon[len(pokemon) - 1])
        pok = list(map(lambda i: i + a if i <= a else i - a, pokemon))
        pokemon = pok
    elif ind > (len(pokemon)-1):
        a = pokemon.pop(len(pokemon) - 1)
        summ += a
        pokemon.append(pokemon[0])
        pok = list(map(lambda i: i + a if i <= a else i - a, pokemon))
        pokemon = pok
    else:
        a = pokemon.pop(ind)
        summ += a
        pok = list(map(lambda i: i + a if i <= a else i - a, pokemon))
        pokemon = pok
print(summ)