# Medium
## 15. 3Sum
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j, i != k, and j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

```
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

# Key Idea
## Approach 1 - Two pointers
1. Sort the arrary → This help in efficiently finding pairs using the Two Pointers technique.
2. Iterate through the array:
    - Fix one element (`nums[i]`)
    - Use the **Two Pointers** technique to find two numbers (`nums[j]` and `nums[k]`) that sum to `-nums[i]`
    - Skip duplicate elements to ensure uniqueness
3. Move left/right pointer based on sum conditions
