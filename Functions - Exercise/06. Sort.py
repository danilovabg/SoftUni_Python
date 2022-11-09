nums = input().split(' ')
def sorted(nums):
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    nums.sort()
    return  nums
print(sorted(nums))
