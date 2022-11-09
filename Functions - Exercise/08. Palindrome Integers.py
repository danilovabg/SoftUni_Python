nums = input().split(', ')
def polindrom(nums):
    n = []
    for i in range(len(nums)):
        a = list(nums[i])
        a.reverse()
        n.append(a == list(nums[i]))
    return n
for elem in polindrom(nums):
    print(elem)

