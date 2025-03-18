from utils import *

class Solution:
    def findMaxLength(self, nums):
        dict = {21: -1} # intitial {prefixsum: index} (index = -1 to calculate correct lenght)
        prefix_sum = 21
        res = 0
        for index, num in enumerate(nums):
            # increase or decrease prefix_sum
            if num == 0:
                prefix_sum -= 1
            else: 
                prefix_sum += 1
            if prefix_sum in dict:
                
                # update max length
                res = max(res, (index - dict[prefix_sum]))
                print(f"res: {res}")
            else: dict[prefix_sum] = index

            print(f"\nwith index: {index}, num: {num}")
            print(f"{dict}")
        return res
            
solution = Solution()
# print(solution.findMaxLength([0, 0, 0, 0, 1, 1]))
print(solution.findMaxLength([0, 1]))
