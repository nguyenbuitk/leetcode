'''
Skip Duplicate Elements in the Outer Loop
    If nums[start] is the same as the previous number, skip it to avoid duplicate triplets.
Skip Duplicate Elements in the Two-Pointer Loop
    After finding a valid triplet, skip consecutive duplicate elements to avoid redundant results.
'''
class Solution(object):
    def threeSum(self, nums):
        # Initialize a set to store unique triples
        res = []
        
        # Step 1: sort the input aray to allow two-pointer traversal
        nums.sort()
        
        # Step 2: Iterate throught the array, choosing each number as potential first element
        for start in range(len(nums) - 2):
            if nums[start] > 0:         # Cause the array sorted, if nums[start] > 0, then sum 3 elements aways > 0
                return res
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            
            l, r = start + 1, len(nums) - 1
            print("l, r", l, r)
            target = -nums[start]
            
            # Step 3: Two pointer approach to find pairs taht sum up to target
            while l < r:
                print(f"travers: {nums[start]}, {nums[l]}, {nums[r]}")
                if nums[l] + nums[r] == target:
                    res.append(nums[start], nums[l], nums[r])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
def check_duplicate(arr1, arr2):
    return set(arr1) == set(arr2)
