from utils import *

def swap(a, b):
    return b, a

class Solution(object):
    def sortColors(self, nums):
        print_list_with_indexes(nums)
        # Initilize pointer
        # l (left) track the last poistion of 0
        # r (right) track the last position of 2
        # m: middle pointer that iterate and process elements
        l, r = -1, len(nums)
        while l < r - 1:
            print(f"l, r: {l}, {r}")
            m = l + 1
            '''
            Handling Each Case
            nums[m] == 0: Move 0 to the left by swapping with l + 1, then increase l.
            nums[m] == 2: Move 2 to the right by swapping with r - 1, then decrease r.
            nums[m] == 1: Keep 1 in place and move m forward.
            '''
            while m < r:
                if nums[m] == 1:
                    m += 1
                    if m == r:
                        return nums
                    continue

                if nums[m] == 2:
                    nums[r - 1], nums[m] = swap(nums[r - 1], nums[m])
                    r -= 1
                    break

                if nums[m] == 0:
                    nums[l + 1], nums[m] = swap(nums[l + 1], nums[m])
                    l += 1
                    break

        return nums

solution = Solution()
print(solution.sortColors([2, 0, 2, 1, 1, 0]))
print(solution.sortColors([0, 0]))
