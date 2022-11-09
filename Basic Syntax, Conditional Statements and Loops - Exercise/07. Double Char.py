st = input()
while True:
    if st == 'End':
        break
    elif st == 'SoftUni':
        pass
    else:
        for i in st:
            print(i*2, end='')
        print()
    st = input()
