# Medium
## 560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

```
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
```

# Key Idea
[Base on this explain](../../02_two_pointer/notes.md), we can know why this problem can't using two pointer or sliding window to solve.
- If a window is valid. E.g sum `[1,2,3]` <= 6, we don't know whether narrow down scope of this window is valid. It can be `> 6` or `< 6`
- So it does not guarantee the rule of two pointer

## Approach 1 Brute force
Calculate every posible subarray, if it sum to k, then res += 1
- Iterate i and j = i + 1 to find all posible subarray

This is not efficient

## Approach 2 Hash Map + Prefix sum

```
Indexes:  0   1   2   3   4   5   6   7
Nums:     3   4   7   2  -3   1   4   2

### Prefixsum
Indexes:  0   1   2   3   4   5   6   7
Nums:     3   7  14  16  13  14  18  20
```
Explain: examine `nums[7] = 2`, we need to find the how many subarray end at index `7` with total `sum = 7`

when `prefix_sum[7] = 20` <=> `nums[0] + nums[1] + nums[2] + ... + nums[7] = 20`

With target = 7, it means we need to find i with `nums[0] + nums[1] + ... + nums[i] = 13` <=> `prefix_sum[i] = 13`. 
So we need to store the previous prefix_sum of value i in dictionary. 

Then check whether prefix_sum exisits with subarray end at index `7`


0 -2 2 7, target = 7
pre -2, 0, 7 -> there will be 2 array

```python

dt = {}     # dictionary for save the index of prefix sum
res = 0     # biến đếm số lượng subarray có tổng bằng k
pref_sum = None
for i in range(len(nums)):
    if pref_sum == None:
        pref_sum = nums[i]        # calcualte prefix sum (sum from start to nums[i])
    else: pref_sum += nums[i]
    
    # if nums[i] == k then target = sum(nums[:i]) -> alwasy exits
    # if target == 0 meaning sum(nums[:i]) == k, but `0` still not exists in dict yet. So we must cover this case
    target = pref_sum - k
    
    if target in dt:
        res += dt[target]
    '''
    Example: Let's say our elements are [1,2,1,3] and k = 3, and our corresponding running sums = [1,3,4,7]
    Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.

    But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why target == 0 comes in the picture.
    '''
    if target == 0:
        res += 1
    dt[pref_sum] = dt.get(pref_sum, 0) + 1
```