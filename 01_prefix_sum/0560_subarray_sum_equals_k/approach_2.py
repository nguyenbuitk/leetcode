from utils import *

class Solution:
    def subarraySum(self, nums, k):
        print_list_with_indexes(nums)
        dt = {}     # dictionary for save the index of prefix sum
        res = 0     # biến đếm số lượng subarray có tổng bằng k
        
        ## for debuging
        prefix_sum = []
        for num in nums:
            if not prefix_sum:
                prefix_sum.append(num)
            else:
                prefix_sum.append(num + prefix_sum[-1])
        print("\n### Prefixsum")
        print_list_with_indexes(prefix_sum)
                
        
        pref_sum = None
        for i in range(len(nums)):
            if pref_sum == None:
                pref_sum = nums[i]        # calcualte prefix sum (sum from start to nums[i])
                
            else: pref_sum += nums[i]
            
            # if nums[i] == k then target = sum(nums[:i]) -> alwasy exits
            # if target == 0 meaning sum(nums[:i]) == k, but `0` still not exists in dict yet. So we must cover this case
            target = pref_sum - k
            
            if target in dt:
                res += dt[target]
            
            if target == 0:
                res += 1
            
            dt[pref_sum] = dt.get(pref_sum, 0) + 1
            print(f"num: {nums[i]}, prefix_sum = {pref_sum} target= {target} res = {res} dict: {dt}")
        return res
            

solution = Solution()
# print(solution.subarraySum([1,1,1], 2))
# print(solution.subarraySum([1,2,3], 3))
print(solution.subarraySum([1,2,1,3], 3))

# print(solution.subarraySum( [3, 4, 7, 2, -3, 1, 4, 2], 7))
# print(solution.subarraySum( [0,0,0,0,0,0,0,0,0,0], 0))
# print(solution.subarraySum([-2,2, 1,0,1], 5))