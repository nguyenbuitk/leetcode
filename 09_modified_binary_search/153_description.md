# Medium
## 153. Find Minimum in Rotated Sorted Array
Suppose an array of length `n` sorted in ascending order is rotated between 1 and n times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.
Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

# Key Idea
**Notes** See the visualize at `33_description.md` for easily understand
## Approach 1
**Similar approach to problems 33, 81**
1. We use `Modified Binary Search` to determine which haft is sorted
2. After that, calculate the min value of sorted haft and move pointer to the remaining haft

## Approach 2 - Optimize
1. We don't need to determine which haft is sorted.
2. We compare the `nums[mid]` to `nums[-1]`
    - If `>` --> move right `(l = mid + 1)`
    - If `<` --> move left `(r = mid)`

## Approach 3 - Community
1. We don't need to determine which haft is sorted.
2. Before we compare the `nums[mid]` to `nums[0]`, if `nums[left] < nums[right]`, return `nums[left]` (to core the case like `[11,12]`)
    - If `nums[mid] >= nums[0]` --> move right `(l = mid + 1)`
    - If `<` --> move left `(r = mid)`