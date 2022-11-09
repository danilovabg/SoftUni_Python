nums = input().split(' ')
def min(nums):
    m = 10000000000
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        if nums[i] < m:
            m = nums[i]
    return m
def max(nums):
    m = -10000000000
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        if nums[i] > m:
            m = nums[i]
    return m
def sum(nums):
    s = 0
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        s += nums[i]
    return s
print(f'The minimum number is {min(nums)}')
print(f'The maximum number is {max(nums)}')
print(f'The sum number is: {sum(nums)}')