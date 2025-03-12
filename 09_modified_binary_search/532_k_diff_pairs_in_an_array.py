from typing import List
from collections import Counter

def findPairs(nums: List[int], k: int) -> int:
    seen = set()
    pair = set()
    for num in nums:
        for target in (num + k, num - k):
            if target in seen and (target, num) not in pair and (num, target) not in pair:
                    pair.add((num, target))
        seen.add(num)
    return len(pair)

# print(findPairs([3,1,4,1,5], 2))
print(findPairs([1,2,4,4,3,3,0,9,2,3], 3))
        
    
        