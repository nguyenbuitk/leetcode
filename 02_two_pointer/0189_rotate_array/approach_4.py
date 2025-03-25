from utils import *

''' with k = 3
1, 2, 3, 4, 5, 6, 7       (nums_old)
            i
5, 6, 7, 1, 2, 3, 4       (nums_new)
j
j = i + 3 
nums_new[j] = nums_old[i]


<=> nums_new[i + 3] = num_old[i]
<=> nums_new[j] = nums_old[j-3]
'''

def rotate(nums: List[int], k: int) -> None:
    if k == 0:
        return
    n = len(nums)
    start = 0
    count_num = 0
    while count_num < n:
        curr = start
        numToBeRotated = nums[start]
        while True:
            print(f"numToBeRotated: {numToBeRotated}")
            print_list_with_indexes(nums, start=start, n_curr=((curr+k)%n))
            temp = nums[(curr +k)%n]
            # print(f"curr+k  % n = {(curr+k)%n}")
            nums[(curr + k)%n] = numToBeRotated
            numToBeRotated = temp
            count_num += 1
            curr += k
            if curr%n == start or count_num == n:
                break
        print(f"nums after circle {start}: {nums}")
        time.sleep(0.3)
        start += 1
    
# rotate([1,2,3,4,5,6,7], 0)
rotate([-1,-100,3,99], 2)

        