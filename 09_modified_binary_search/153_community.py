def findMin(nums) -> int:

    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left]  < nums[right]:
            return nums[left]
        mid = (left + right) // 2
        print(f"l: {left}, r: {right}, m: {mid}")
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

print(findMin([0,1,2,3]))