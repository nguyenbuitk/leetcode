from utils import *

def nextPermuation(nums: List[int]) -> None:
    print_list_with_indexes(nums)
    # Step 1: find the pivot
    n = len(nums)
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    if pivot == -1:
        nums.reverse()
        return
    
    # Step 2: swap with greater than pivot but smallest in subarray
    for i in range(n - 1, -1 , -1):
        if nums[i] > nums[pivot]:
            print(f"i: {i}")
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
    
    # Step 3: sort the subarray
    i, j = pivot + 1, n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    
    print(f"pivot is {pivot}")
    print(f"nums: {nums}")
    
# nextPermuation([3, 2, 5, 4, 1])
nextPermuation([1, 2, 3])