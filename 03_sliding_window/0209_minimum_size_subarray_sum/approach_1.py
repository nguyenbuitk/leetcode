from utils import *
class Solution:
    def minSubArrayLen(self, target, nums):
        left, res = 0, float('inf')
        sum = 0
        for right in range(len(nums)):

            if nums[right] >= target:
                return 1
            # expand window
            sum += nums[right]

            # shrink window
            while sum >= target:
                res = min(right - left + 1, res)
                sum -= nums[left]
                left += 1
                
        if res == float('inf'):
            return 0
        return res
solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))