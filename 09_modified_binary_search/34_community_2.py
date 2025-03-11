from utils import print_nums_with_indexes

def findGreaterEqual(nums, target):
    print_nums_with_indexes(nums)
    l, r = 0, len(nums) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            if nums[m] == target:
                res = m
            r = m - 1
    return res

print(findGreaterEqual([4,5,5,6,7], 5))