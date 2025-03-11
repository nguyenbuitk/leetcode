from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    # find min k:
    # sum((piles[i] // k) + 1) == h
    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        print(f"low: {low}, high: {high}, mid: {mid}")
        total_hours = sum((pile + mid - 1)//mid for pile in piles)
        print(f"total_hour: {total_hours}")
        if total_hours <= h:
            high = mid
        else:
            low = mid + 1
    return low
print(minEatingSpeed([312884470], 968709470))