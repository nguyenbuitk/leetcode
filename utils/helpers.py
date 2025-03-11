from typing import List

def print_nums_with_indexes(nums: List[int]):
    indexes = list(range(len(nums)))
    
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
