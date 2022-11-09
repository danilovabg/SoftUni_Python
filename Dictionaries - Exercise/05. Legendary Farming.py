element_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
while max(element_dict.values()) < 250:
    line = input().lower().split()
    for i in range(1, len(line), 2):
        if line[i] in element_dict:
            element_dict[line[i]] += int(line[i-1])
        elif line[i] in junk:
            junk[line[i]] += int(line[i - 1])
        else:
            junk[line[i]] = int(line[i - 1])
        if max(element_dict.values()) >= 250:
            Done = True
            break


if element_dict["shards"] >= 250:
    item = "Shadowmourne"
    element_dict['shards'] -= 250
elif element_dict['fragments'] >= 250:
    item = "Valanyr"
    element_dict['fragments'] -= 250
elif element_dict['motes'] >= 250:
    item = "Dragonwrath"
    element_dict['motes'] -= 250

print(f"{item} obtained!")
[print(f"{el}: {value}") for el, value in element_dict.items()]
[print(f"{el}: {value}") for el, value in junk.items()]
