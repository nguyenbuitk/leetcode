from utils import *

def rotate(nums: List[int], k: int) -> None:
    print_list_with_indexes(nums)
    n = len(nums)
    k = k % n
    if k == 0:
        return

    
# move last 3 number
rotate([1,2,3,4,5,6,7], 2)
# [1,2,3,4,5,6,7]
# [1,2,3,4,5,7,6]
# [6,7,3,4,5,1,2]
# [6,7,5,4,3,1,2]
# [6,7,1,2,3,4,5]

# [1,2,3,4,5,6,7]
# [7,6,5,4,3,2,1]

# [1,2,3,4,7,6,5]
# [5,6,7,4,1,2,3]
# [5,6,7,4,1,2,3]

# [6,7,1,2,3,4,5]



