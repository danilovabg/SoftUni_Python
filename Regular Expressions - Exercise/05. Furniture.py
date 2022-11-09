import re
line = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.*\d*)!(\d+)'
cost = 0
furniture = []
print('Bought furniture:')
while line != 'Purchase':
    res = re.findall(pattern, line)
    try:
        cost += float(res[0][1])*float(res[0][2])
        print(res[0][0])
    except IndexError:
        pass
    line = input()

print(f"Total money spend: {cost:.2f}")


# import re
#
# main_string = input()
#
# pattern = re.compile(
#     r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)")
#
# total_money_spend = 0
# print("Bought furniture:")
# while main_string != "Purchase":
#     result = re.finditer(pattern, main_string)
#     for show in result:
#         total_money_spend += float(show["price"]) * float(show["quantity"])
#         print(show["furniture_name"])
#     main_string = input()
#
# print(f"Total money spend: {total_money_spend:.2f}")