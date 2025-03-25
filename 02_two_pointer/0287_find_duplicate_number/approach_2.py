from utils import *
def findDuplicate(nums: List[int]) -> int:
    
    for idx, val in enumerate(nums):
        print(f"val: {val}, idx: {idx}")
        val = abs(val)
        if nums[val] < 0:
            return abs(val)
        else: 
            nums[val] = -nums[val]
        print_list_with_indexes(nums)

        
print(findDuplicate([1,3,4,2,2]))