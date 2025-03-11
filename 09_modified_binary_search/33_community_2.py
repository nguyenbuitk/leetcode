from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            m = (l + r) // 2
            print(f"l: {l}, r: {r}, m: {m}")
            if nums[m] == target:
                 return m
            
            # if target in the same haft with nums[m]. Note that we must have the "=" sign
            if (nums[m] >= nums[0]) == (target >= nums[0]):
                print("target in the same haft with nums[m]")
                num = nums[m]
            
            # if target in the right haft, nums[m] in the left haft. Assign num = float ('-inf') for moving the the right when compare 
            elif nums[m] > target:
                num = float('-inf')
            # target in the left haft, num[m] in the right haft
            else:
                num = float('inf')
            
            print(f"num = {num}")
            # compare and move to right
            if target > num:
                l = m + 1
            else: r = m - 1
        return -1

solution = Solution()
solution.search([1,3], 3)