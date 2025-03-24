from utils import *

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

def rotate(nums: List[int], k: int) -> None:
    if k == 0:
        return
    start = 0
    print_list_with_indexes(nums)
    while start < k:
        curr = start
        numToBeRotated = nums[curr]
        while curr + k < len(nums):
            curr += k
            temp = nums[curr]
            nums[curr] = numToBeRotated
            numToBeRotated = temp
        print(f"nums after circle {start}: {nums}")
        time.sleep(0.3)
        start += 1
    
rotate([1,2,3,4,5,6,7], 3)
        