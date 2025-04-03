from utils import *

def findLHS(nums: List[int]) -> int:
    res = 0
    count = Counter(nums)
    print(count)
    for key, val in count.items():
        if count[key+1]:
            print(f"with {key}, max_length is {val + count[key + 1]}")
        else:
            print(f"with {key}, max_lenght is {val}")
        res = max(res, val + count.get(count[key + 1], float('-inf')))
        
    return res
print(findLHS([1,3,2,2,5,2,3,7]))