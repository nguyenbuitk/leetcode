from typing import List
from collections import defaultdict
from utils import print_list_with_indexes


def longestArithSeqLength(nums: List[int]) -> int:
    print_list_with_indexes(nums)
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    dp[0] = {}
    max_length = 1
    for i in range(1, n):
        for j in range(i):
            print(f"\ni = {i}, j = {j}")
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            
            max_length = max(max_length, dp[i][diff])
            print(f"dp[{i}]: {dp[i]}")

    res = []
    for i in range(1, n):
        print(f"dp[{i}]: {dp[i]}")
        res.append(max(dp[i].values()))
    return(max(res))
    
print(longestArithSeqLength([20,1,15,3,10,5,8]))
    