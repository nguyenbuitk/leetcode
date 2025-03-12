def maximumCount(nums):
    # find the first negative
    l, r = 0, len(num) - 1
    index_neg = 0 
    index_pos = 0
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= 0:
            r = m - 1
        else:
            index_neg = m
            l = m + 1
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r ) // 2
        if nums[m] <= 0:
            l = m+1
        else:
            index_pos = len(nums) - m
            r = m -1
    return max(index_neg, index_pos)



