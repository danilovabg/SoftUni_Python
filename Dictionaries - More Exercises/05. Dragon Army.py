dragon_list = []
num = int(input())
while num > 0:
    new_type = True
    drag = input().split()
    if drag[2] == 'null':
        drag[2] = 45
    else:
        drag[2] = int(drag[2])
    if drag[3] == 'null':
        drag[3] = 250
    else:
        drag[3] = int(drag[3])
    if drag[4] == 'null':
        drag[4] = 10
    else:
        drag[4] = int(drag[4])
    for el in dragon_list:
        if drag[0] in el:
            el[drag[0]][drag[1]] = [drag[2], drag[3], drag[4]]
            new_type = False
    if new_type:
        dragon_list.append({drag[0]: {drag[1]: [drag[2], drag[3], drag[4]]}})
    num -= 1
# print(dragon_list)
for element in dragon_list:
    for ty, dr in element.items():
        av_demage, av_health, av_armor = 0, 0, 0
        print(f"{ty}::", end='')
        for na, spec in dr.items():
            av_demage += spec[0]
            av_health += spec[1]
            av_armor += spec[2]
        print(f"({av_demage/len(dr):.2f}/{av_health/len(dr):.2f}/{av_armor/len(dr):.2f})")
        dr = sorted(dr.items())
        for ind, item in enumerate(dr):
            print(f"-{dr[ind][0]} -> damage: {dr[ind][1][0]}, health: {dr[ind][1][1]}, armor: {dr[ind][1][2]}")
#
# import weakref
#
# class Dragons:
#     def __init__(self, type):
#         self.type = type
#         self.type_list = []
#
#     def add_dragon(self, name, damage, health, armor):
#         self.name = name
#         self.damage = damage
#         self.health = health
#         self.armor = armor
#         self.type_list.append((name, damage, health, armor))
#
#     def __repr__(self):
#         return f"dragon type {self.type}: {self.type_list}."
# dragon_type = set()
# num = int(input())
# while num > 0:
#     drag = input().split()
#     drag[0] = Dragons(drag[0])
#     dragon_type.add(drag[0])
#     if drag[2] == 'null':
#         drag[2] = 45
#     else:
#         drag[2] = int(drag[2])
#     if drag[3] == 'null':
#         drag[3] = 250
#     else:
#         drag[3] = int(drag[3])
#     if drag[4] == 'null':
#         drag[4] = 10
#     else:
#         drag[4] = int(drag[4])
#     drag[0].add_dragon(drag[1], drag[2], drag[3], drag[4])
#     num -= 1
# print(dragon_type)
# print(vars(Dragons))
#
