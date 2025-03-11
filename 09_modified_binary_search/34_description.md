# Medium
## 34. Find First and Last Position of Element in Sorted Array
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If target is not found in the array, return `[-1, -1]`.
You must write an algorithm with `O(log n)` runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

# Key Idea
## Approach 1 - Optimize
1. Binary Search for the First Occurrence
    - Perform binary search to locate the first index of the target.
    - If `nums[mid] == target`, store midand continue search toward to the left to find the first occurence
2. Do similar to perform binary search for the last occurence

## Approach 2 - Self
1. Perform bianry search to locate the target
    - If found, set both `min_pos` and `max_pos` to this position
2. Scan left and right to find the first and last occurence

**Notes**: Linear scan `O(n)` after binary search make it less optimal than a pure `O(log n)` solution

## Approach 3 - Community 1 
**[Link solution](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/14699/clean-iterative-solution-with-two-binary-searches-with-explanation/)**
1. Using 2 binary search to find the left most and right most target
    - In case of find left most, if `target == nums[m]` we will store this potential `m` value and move to right with `l = mid + 1`
    - Do similar to find the right most target

## Approach 4 - Commnuity 2
**[Link solution](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/14701/a-very-simple-java-solution-with-only-one-binary-search-algorithm/)**
1. Define a helper function `findGreaterEqual(nums)` to find the first greater equal than `target`, it not found it will return `len(nums)`
    - In this function, we will define `l, r = 0, len(nums)` instead of `r = len(nums) - 1`
2. We will call `findGreaterEqual()` two times
    - first time call `findGreaterEqual(nums, target)` to find the left most
    - second time call `findGreaterEqual(nums, target + 1)` to find the right most

**Example**
```python
nums = [5,7,7,8,8,10]
target = 8
```
**Step 1: Find `start`**
- `firstGreaterEqual(nums, 8) → 3`
- So, `start = 3` (first occurrence of `8`).

**Step 2: Find `end`**
- `firstGreaterEqual(nums, 9) → 5` (first index where `nums[i] >= 9`).
- `end = 5 - 1 = 4` (last occurrence of `8`).

**Output:** `[3, 4]`