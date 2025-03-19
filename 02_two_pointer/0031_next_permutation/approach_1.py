# Most people look from front to back, but looking in the opposite direction can provide useful solutions.
from utils import *

def next_permutation(lst):
    """
    Generates the next permutation in lexicographical order.
    Modifies the list in-place to the next permutation.
    Returns False if no next permutation exists (i.e., last permutation).
    """
    n = len(lst)
    k = -1

    # Step 1: Find the largest index k such that lst[k] < lst[k+1]
    for i in range(n - 2, -1, -1):
        if lst[i] < lst[i + 1]:
            k = i
            break

    # If no such k exists, we are at the last permutation
    if k == -1:
        return False

    # Step 2: Find the largest index l greater than k such that lst[k] < lst[l]
    l = -1
    for i in range(n - 1, k, -1):
        if lst[i] > lst[k]:
            l = i
            break

    # Step 3: Swap elements at k and l
    lst[k], lst[l] = lst[l], lst[k]

    # Step 4: Reverse the sequence from k+1 to end
    lst[k + 1:] = reversed(lst[k + 1:])

    return True

def print_permutations_lexicographically(lst):
    """
    Prints all permutations of the given list in lexicographical order.
    """
    # Step 1: Sort the list to ensure lexicographical order
    lst.sort()
    
    # Step 2: Print the first permutation
    print(lst[:])
    
    # Step 3: Generate and print next permutations until there are none left
    while next_permutation(lst):
        print(lst[:])

# Example usage


class Solution(object):
    def nextPermutation(self, nums):
        
        k = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break

        if k == -1:
            nums.reverse()
        print("k: ", k)

        min_index = k + 1
        for i in range(k + 2, len(nums)):
            if nums[i] < nums[min_index] and nums[i] > nums[k]:
                min_index = i
        print("min_index: ", min_index)

        nums[k], nums[min_index] = nums[min_index], nums[k]
        res_arr = nums[k + 1:]
        res_arr.sort()
        
        for i in range(len(res_arr)):
            nums[k + i + 1] = res_arr[i]

        print("nums: ", nums)
        print("res_arr: ", res_arr)


solution = Solution()
nums = [1, 5, 1]
nums2 = [3, 2, 5, 4, 1]
print_permutations_lexicographically(nums2)
#solution.nextPermutation(nums)

