from typing import List, Dict, Optional
from collections import deque
import time

def print_list_with_indexes(nums: List[int], **pointers: Dict[str,int]):
    COLUMN_WIDTH = 5
    indexes = [i for i in range(len(nums))]
    out_of_range = []
    nums_str = "".join(str(num).center(COLUMN_WIDTH) for num in nums)
    indexes_str = "".join(str(i).center(COLUMN_WIDTH) for i in indexes)

    # arrow lines
    arrows = [" " * COLUMN_WIDTH] * len(nums)
    for var_name, idx in pointers.items():
        # print(f"var_name: {var_name}, idx: {idx}")
        if 0 <= idx < len(nums):
            arrows[idx] = "  ↑  "
    arrows_str = "".join(arrows)
    
    # variable line
    names = [" " * COLUMN_WIDTH] * len(nums)
    for var_name, idx in pointers.items():
        if 0 <= idx < len(nums):
            if names[idx].strip():
                names[idx] = names[idx].strip() + "," + var_name
            else:
                names[idx] = var_name
        else:
            out_of_range.append((var_name, idx))
            
    names_str = "".join(name.center(COLUMN_WIDTH) for name in names)
    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")

    if not arrows_str.isspace():
        print(f"        {arrows_str}")
        print(f"        {names_str}")
    for var, idx in  out_of_range:
        print(f"{var}: {idx} is out of range")
    print("")
    

# print_list_with_indexes([5, 10, 300], i =1, j = -1)
