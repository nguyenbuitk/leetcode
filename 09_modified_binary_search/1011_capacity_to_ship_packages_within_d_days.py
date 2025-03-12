from utils import print_list_with_indexes
from typing import List
import time
def shipWithinDays(weights: List[int], days: int) -> int:
    low, high = max(weights), sum(weights)
    while low < high:
        day = 0
        mid = (low + high) // 2 # capacity
        print(f"\nlow: {low}, high: {high}, mid: {mid}")

        current_capacity = 0
        for weight in weights:
            print(f"day: {day}, current_capacity: {current_capacity}")

            current_capacity += weight
            if current_capacity < mid:
                continue
            elif current_capacity > mid:
                day += 1
                current_capacity = weight
            else:
                day+=1
                current_capacity = 0
        if current_capacity != 0:
            day += 1
        print(f"With capacity: {mid} number of day is {day}")
        
        if day <= days:
            high = mid
        else:
            low = mid + 1
        
        time.sleep(0.5)
    
    return low

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))