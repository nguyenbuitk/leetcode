''' with k = 3
1, 2, 3, 4, 5, 6, 7       (nums_old)
            i
5, 6, 7, 1, 2, 3, 4       (nums_new)
j
j = i + 3 
nums_new[j] = nums_old[i]


<=> nums_new[i + 3] = num_old[i]
<=> nums_new[j] = nums_old[j-3]
'''
from utils import *

def rotate(nums: List[int], k: int) -> None:
    k = k % len(nums)
    if k == 0:
        return
    
    nums_old = []
    for num in nums:
        nums_old.append(num)
    
    for i in range(len(nums)):
        nums[i] = nums_old[i-k]

rotate([1,2,3,4,5,6,7], 3)