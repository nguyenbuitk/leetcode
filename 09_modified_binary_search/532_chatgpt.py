from typing import List
from collections import Counter

def findPairs(nums: List[int], k: int) -> int:
    seen = set()
    pairs = set()

    for num in nums:
        if num - k in seen:
            pairs.add((num - k, num))
        if num + k in seen:
            pairs.add((num, num + k))
        seen.add(num)
    print(pairs)
    return len(pairs)

# print(findPairs([3,1,4,1,5], 2))
print(findPairs([1,2,4,4,3,3,0,9,2,3], 3))
        
    
        