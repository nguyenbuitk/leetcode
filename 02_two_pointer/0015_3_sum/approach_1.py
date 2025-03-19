class Solution(object):
    def threeSum(self, nums):
        # Initialize a set to store unique triples
        res = set()
        
        # Step 1: sort the input aray to allow two-pointer traversal
        nums.sort()
        
        # Step 2: Iterate throught the array, choosing each number as potential first element
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            
            l, r = start + 1, len(nums) - 1
            print("l, r", l, r)
            target = -nums[start]
            
            # Step 3: Two pointer approach to find pairs taht sum up to target
            while l < r:
                print(f"travers: {nums[start]}, {nums[l]}, {nums[r]}")
                if nums[l] + nums[r] == target:
                    arr = (nums[start], nums[l], nums[r])
                    res.add(arr)
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return [list(triple) for triple in res]

def check_duplicate(arr1, arr2):
    return set(arr1) == set(arr2)
