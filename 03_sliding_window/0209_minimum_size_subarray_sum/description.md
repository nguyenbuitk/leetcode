# Medium
## 209. Minimum Size Subarray Sum
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

# Key Idea
## Approach: Slinding Window
1. Use Two Pointer
    - The `right` pointer expands the windows to include new elements
    - The `left` pointer shrink the window when sum is greater or equal than target
2. Maintain the windows
    - Maintain the minimal length when iterate the array

### Notes
The following rules must be satisfied for problems that can be solved using the `sliding windows` method
1. If a wider window is valid, the narrow of that wider scope is valid
2. If a narrower window is invalid, the wider scope of that narrow scope is invalid

In this problem, `valid` mean `has sum smaller than target`. Then 2 rules is rewriten as follows:
1. If a wider window has sum smaller than target, the the narrow window has um smaller than target
2. If a narroer window has sum smaller than target, the wider scope is not sure has sum larger than target