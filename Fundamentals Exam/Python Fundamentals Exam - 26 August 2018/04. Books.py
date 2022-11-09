book = input()
store = {}

while book != 'on work':
    validation = book.split('->')
    if len(validation) > 1 and len(validation[1]) > 1:
        try:
            name, author, price = validation[0].split()
            chapters = len(validation[1].split(','))
        except ValueError:
            pass
        else:
            try:
                price = float(price)
                if price > 0:
                    store[name] = (author, price, chapters)
            except ValueError:
                pass
    book = input()

sold_list = []
by_book = input()
day_summ = 0
while by_book != 'end work':
    if by_book in store:
        sold_list.append(by_book)
        day_summ += store[by_book][1]
    else:
        print('No such book here')
    by_book = input()

if len(sold_list) > 0:
    for book in sold_list:
        print(f"SOLD: {book} with author {store[book][0]}. Chapters in the book {store[book][2]}")
if day_summ == 0:
    print('Bad day :(')
else:
    print(f"Money: {day_summ:.2f}")
