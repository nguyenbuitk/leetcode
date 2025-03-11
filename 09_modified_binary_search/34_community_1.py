from typing import List
from utils import print_nums_with_indexes

def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1,-1]
    res = [-1,-1]
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        # if nums[m] == target, move to the left to find the left most position
        if nums[m] >= target:
            if nums[m] == target:
                res[0] = m          # store potential position
            r = m - 1
        else:
            l = m + 1
            
    if nums[l] == target: res[0] = l
    l, r = 0, len(nums) - 1
    while l < r:

        m = (l + r) // 2
        if nums[m] <= target:
            if nums[m] == target:
                res[1] = m
            l = m + 1
        else:
            r = m - 1
    if nums[l] == target: 
        res[1] = l
    return res