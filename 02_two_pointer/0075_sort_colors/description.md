# Medium
## 75. Sort Colors
Given an array `nums` with `n` objects colored red, white, or blue, sort them `in-place` so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
```
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

# Key Idea
## Approach 1 - Self
Pointers (l, r, m)
- `l`: Tracks the last position of 0 (Red).
- `r`: Tracks the first position of 2 (Blue).
- `m`: Middle pointer that iterates and processes elements.

Handling Each Case
- nums[m] == 0: Move 0 to the left by swapping with l + 1, then increase l.
- nums[m] == 2: Move 2 to the right by swapping with r - 1, then decrease r.
- nums[m] == 1: Keep 1 in place and move m forward.

## Approach 2 - Chat GPT - Ductch National Flag
**Optimize version of approach 1**
### [Link script](./approach_2.py)