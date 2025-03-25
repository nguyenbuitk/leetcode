from typing import *
def findDuplicate(nums: List[int]):
    count = [0]*len(nums)
    for idx, val in enumerate(nums):
        count[val] += 1
        if count[val] > 1:
            return val
        