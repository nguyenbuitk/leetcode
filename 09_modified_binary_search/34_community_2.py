def findGreaterEqual(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

def searchRange(nums, target):
    firstPos = findGreaterEqual(nums, target)
    if firstPos == len(nums) or nums[firstPos] != target:
        return [-1,-1]
    return [firstPos, findGreaterEqual(nums, target+1) - 1]

print(findGreaterEqual([5,7,7,8,8,10], 9))
#print(findGreaterEqual([1], 4))