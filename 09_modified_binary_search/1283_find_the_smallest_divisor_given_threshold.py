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
