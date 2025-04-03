from utils import *

def longestOnes(A: List[int], K: int) -> int:
    left = right = 0
    
    for right in range(len(A)):
        print_list_with_indexes(A, l=left, r= right)
    # if we encounter a 0 the we decrement K
        if A[right] == 0:
            K -= 1
        # else no impact to K
        
        # if K < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if K < 0:
            # if the left one was zero then we adjust K
            if A[left] == 0:
                K += 1
            # regardless of whether we had a 1 or a 0 we can move left side by 1
            # if we keep seeing 1's the window still keeps moving as-is
            left += 1
            print_list_with_indexes(A, l=left, r= right)
    
    return right - left + 1
        
longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)