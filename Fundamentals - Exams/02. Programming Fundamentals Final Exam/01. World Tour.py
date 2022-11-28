start_stops = list(input())

stops = input()
while stops != 'Travel':
    stops = stops.split(':')
    if stops[0] == 'Add Stop' and int(stops[1]) <= len(start_stops):
        for i, el in enumerate(list(stops[2])):
            start_stops.insert(int(stops[1])+i, el)
    elif stops[0] == 'Remove Stop':
        ind1, ind2 = int(stops[1]), int(stops[2])
        if ind1 < len(start_stops) and ind2 < len(start_stops):
            start_stops = start_stops[:ind1] + start_stops[ind2+1:]
    elif stops[0] == 'Switch':
        str = ''.join(start_stops)
        if stops[1] in str:
            start_stops = list(str.replace(stops[1], stops[2]))
    print(''.join(start_stops))
    stops = input()
str = ''.join(start_stops)
print(f'Ready for world tour! Planned stops: {str}')