# Medium
## 189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

```
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

# Key Idea
## Approach 1 Self
**`O(n) time, O(n) space`**
```
# Create new_nums       [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
# Revert new_nums       [5, 6, 7, 1, 2, 3, 4, 1, 1, 1]
# Cut new_nums          [5, 6, 7, 1, 2, 3, 4]
```

## Approach 2
**`O(n) time, O(n) space`**

**Explain with k = 3**
```
''' with k = 3
1, 2, 3, 4, 5, 6, 7       (nums_old)
            i
5, 6, 7, 1, 2, 3, 4       (nums_new)
j
j = i + 3 
nums_new[j] = nums_old[i]

<=> nums_new[i + 3] = num_old[i]
<=> nums_new[j] = nums_old[j-3]
```

## Approach 3
**`O(n) time, O(1) space`**

**Initial array with k = 3**\
`[1, 2, 3, 4, 5, 6, 7]`

1. Revert array
`[7, 6, 5, 4, 3, 2, 1]`

2. Revert `0 -> k` (not include)
`[5, 6, 7, 4, 3, 2, 1]`

3. Revert `k -> end`
`[5, 6, 7, 1, 2, 3, 4]`

## Apporach 4
With the explain of approach 2
