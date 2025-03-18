class Solution:
    def findMaxLength(sef, nums):
        dict = {0: -1} # intitial {prefixsum: index} (index = -1 to calculate correct lenght)
        prefix_sum = 0
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
        return res
            
solution = Solution()
print(solution.findMaxLength([0, 0, 0, 0, 1, 1]))
