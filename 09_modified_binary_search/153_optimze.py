from utils import print_list_with_indexes

def findMin(nums) -> int:
    print_list_with_indexes(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        print(f"l: {left}, r: {right}, m: {mid}")
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
print(findMin([0,1,2,3]))