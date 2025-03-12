import time

def minDays(bloomDay, m: int, k: int) -> int:
    n = len(bloomDay)
    if n < m*k:
        return -1
    # number of day from 1 to n
    # if nubmer of buquet of day mid >= k, then we can reduce the number of day
    left, right = 1, max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")
        adjacent_flower = 0
        number_of_buquet = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                adjacent_flower += 1
                if adjacent_flower == k:
                    number_of_buquet += 1
                    adjacent_flower = 0
            else:
                adjacent_flower = 0
        print(f"with {mid} day, number of bouquet is {number_of_buquet}")
        
        if number_of_buquet < m:
            left = mid + 1
        else:
            right = mid
        time.sleep(0.5)
    return left
    
    
# print(minDays([1,10,3,10,2],3,1))
# print(minDays([7,7,7,7,12,7,7], 2,3))
# print(minDays([1,10,3,10,2], 3,1))
print(minDays([1,2,4,9,3,4,1], 2,2))