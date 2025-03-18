# Medium
## 238. Product of Array Except Self
Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

```
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

# Key Idea
## Approach 1
1. Instead of removing `nums[i]`, and recomputing the product (which is too slow), we can split the product into two parts:
    - Prefix product: the product of all elemnts before i
    - Suffix product: the product of all elements after i
2. We can use 2 arrays to store the prefix and suffix product

## Approach 2.
Smilar to approach 1 but we only use 1 arrays to store the prefix, and then calulate the suffix, added to the array instead of create 2 arrays
```python
n = len(nums)
res = [1]*n

# Step 1: store the prefix first
for i in range(1, n):
    res[i] = res[i-1]* nums[i-1]
print(res)
subfix_product = nums[n-1]

# Step 2: product the suffix
for i in range(n - 2, -1, -1):
    res[i] = res[i] * subfix_product
    subfix_product *= nums[i]
print(res)

return res
```
