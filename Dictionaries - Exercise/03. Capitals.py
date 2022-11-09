country = input().split(', ')
capitals = input().split(', ')
dictionary = dict(zip(country, capitals))

[print(f"{coun} -> {cap}") for coun, cap in dictionary.items()]