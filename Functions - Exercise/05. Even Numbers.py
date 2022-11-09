nums = input().split(' ')
def filter(nums):
    even = []
    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            even.append(int(nums[i]))
    return even
print(filter(nums))