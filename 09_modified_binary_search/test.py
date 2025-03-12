from typing import List

def print_nums_with_indexes(nums: List[int]):
    indexes = list(range(len(nums)))

    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")

def smallestDivisor(nums: List[int], threshold: int):
    low, high = 1, max(nums)
    res = 1
    while low < high:
        mid = (low + high) // 2
        sum_val = sum((num + mid - 1) // mid for num in nums)
        if sum_val > threshold:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res

