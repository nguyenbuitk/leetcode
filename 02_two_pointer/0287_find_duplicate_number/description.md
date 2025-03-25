# Medium
## 287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
 
```
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
```

# Key Idea
## Approach 1 - Using Linked List
### [Details Explain](https://www.youtube.com/watch?v=wjYnzkAhcNk&t=443s)
**Code**
```python
    slow = nums[0]
    # fast = fast.next.next
    fast = nums[nums[0]]
    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    slow2 = nums[0]
    slow = nums[slow]
    while slow != slow2:
      slow = nums[slow]
      slow2 = nums[slow2]

    return slow2
```

## Approach 2
**Time O(n) Space O(1)** but not satisfy the requirements (not modify nums)
Since all values of the array are between `[1…n]` and the array size is `n+1`.
while scanning the array from left to right, we set the `nums[n]` to its negative value.
```python
for idx, val in enumerate(nums):
    val = abs(val)
    if nums[val] < 0:
        return abs(val)
    else: 
        nums[val] = -nums[val]
    print_list_with_indexes(nums)
```

## Approach 3
**Count array**
```python
count = [0]*len(nums)
for val in nums:
    count[val] += 1
    if count[val] > 1:
        return val         
```

## Approach 4
**Hash table**
```python
dict = Counter(nums)
for key, val in dict.items():
    if val > 1:
        return key
```