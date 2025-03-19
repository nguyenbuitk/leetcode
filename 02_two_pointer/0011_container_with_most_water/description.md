# Medium
## 11. Container With Most Water
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

```
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```
![Visualize](../images/question_11.jpg)

# Key Idea
## Approach 1 - Brute force
1. Traverse all posible pair of array height to find the max area

## Approach 2 - Two pointers
To apply the concept of 
`1. If a wider window is valid, the narrow of that wider scope is valid`
`2. If a narrower window is invalid, the wider scope of that narrow scope is invalid`

`Valid` in this problem means `max area of water with vertical line i`. 
- If a `window [i:j]` has max area of with vertical line `i`. then if we narrow the window to `[i:j-1]`, the area can only remain the same or decrease. then we don't need to consider the window [i:j-1]
- If a `window [i:j]` don't have max area, then expanding to `[i:j+1]` will not necessarily increase the area

```python
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
```