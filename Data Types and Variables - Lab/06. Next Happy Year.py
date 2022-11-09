
#find_number = False
#duplicated_number = set()
#if year == 0:
#    print('1')
#else:
 #   for y in range(year, 10000000000):
 #y = str(y)
  #      duplicated_number.clear()
   #     for i in y:
    #        duplicated_number.update(y)
     #   if len(duplicated_number) == len(str(year)):
      #      print(y)
       #     find_number = True
        #    break
      #  if find_number:
         #   break
y = int(input())
year = y+1
while True:
    year_dic = {}
    for i in str(year):
        year_dic.update({i: i})
    if len(year_dic.keys()) == len(str(y)):
        break
    else:
        year = int(year)
        year += 1
print(year)