from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot_index = l
        n = len(nums)
        l, r = 0, len(nums) - 1

        while(l <= r):
            m = (l + r) // 2
            real_mid = (m + pivot_index) % n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                r = m -1
            else:
                l = m + 1
        return -1