s = list(input())
newstring = s.copy()

for el in newstring:
    try:
        x = int(el)
        s.remove(el)
    except ValueError:
        break

string = ''.join(s)
x = 0
new = ''
el = ''
end = False
for i in range(len(string)):
    if i == len(string)-1:
        end = True
    try:
        s = int(string[i])
        if len(el) == 0:
            el = string[x:i]
            x = i
    except ValueError:
        if len(el) != 0:
            n = int(string[x:i])
            new += el.upper()*n
            n = 0
            el = ''
            x = i
    if end:
        n = int(string[x:])
        new += el.upper()*n
if x < len(string)-1 and end is False:
    new += string[x:].upper()
unique = set(new)
print(f"Unique symbols used: {len(unique)}")
print(new)

# new = ''
# a=''
# for ind in range(len(string)):
#     sym = string[ind]
#     try:
#         sym = int(sym)
#         sym2 = 0
#         if ind != len(string)-1:
#             try:
#                 sym2 = int(string[ind+1])
#             except ValueError:
#                 pass
#         if sym2 != 0:
#             n = int(str(sym) + str(sym2))
#         else:
#             n = sym
#         new += a.upper()*n
#         a = ''
#         n = 0
#     except ValueError:
#         a += sym
# unique = set(new)
# print(f"Unique symbols used: {len(unique)}")
# print(new)
# new = ''
# a=''
# for ind in range(len(string)):
#     sym = string[ind]
#     try:
#         sym = int(sym)
#         sym2 = 0
#         if ind != len(string)-1:
#             try:
#                 sym2 = int(string[ind+1])
#             except ValueError:
#                 pass
#         if sym2 != 0:
#             n = int(str(sym) + str(sym2))
#         else:
#             n = sym
#         new += a.upper()*n
#         a = ''
#         n = 0
#     except ValueError:
#         a += sym
# unique = set(new)
# print(f"Unique symbols used: {len(unique)}")
# print(new)