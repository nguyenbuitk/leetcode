from utils import *

def applyOperation(nums: List[int]) -> List[int]:
    print_list_with_indexes(nums)
    # value to be move to
    queue = deque([])
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            continue
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            queue.append(i)
        else:
            if queue:
                idx = queue.popleft()
                nums[idx], nums[i]  = nums[i], nums[idx]
                queue.append(i)
        
    return nums
# 22 -> 4 0
# 20 -> 2 0
# 00 -> 0 0
#     
print(applyOperation([1, 2,2, 1,1,0]))