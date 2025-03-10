from typing import List
import time
def search(nums: List[int], target: int) -> int:
    # Tạo danh sách index
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    
    l, r = 0, len(nums) - 1

    
    while(l < r):
        # Step 1: Find pivot (the smallest number)
        print(f"l: {l}, r: {r}")
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
        time.sleep(0.5)
    pivot_index = l
    print(f"pivot: {pivot_index}")
 
    n = len(nums)
    res = nums[:pivot_index]
    nums = nums + res
    l, r = pivot_index, len(nums) - 1
    print(f"nums: {nums}")
    while(l <= r):
        m = (l + r) // 2
        print(f"l: {l}, r: {r}, m: {m}")
        if nums[m] == target:
            return m % n
        elif nums[m] > target:
            r = m -1
        else:
            l = m + 1
    return -1

print(search([3,1], 3))