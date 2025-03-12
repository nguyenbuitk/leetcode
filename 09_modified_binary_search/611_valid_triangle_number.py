from typing import List
from utils import print_list_with_indexes

def triangleNumber(nums: List[int]):
    nums.sort(reverse=True)
    res = 0
    for i in range(len(nums) - 1):
        j = i + 1
        k = len(nums) - 1
        while k > j:
            if nums[k] + nums[j] > nums[i]:
                res += k -j
                j += 1
            else:
                k -= 1
    return res

print(triangleNumber([4,2,3,4]))
