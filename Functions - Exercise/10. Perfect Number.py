#divlist = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
num = int(input())
div = []
def perfect(num):
    z = ''
    if num >= 0:
        for i in range(1, num):
            if num % i == 0:
                div.append(i)
    else:
        z = "It's not so perfect."
    if sum(div) == num:
        z = 'We have a perfect number!'
    else:
        z = "It's not so perfect."
    return z
print(perfect(num))