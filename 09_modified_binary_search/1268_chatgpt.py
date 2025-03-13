from typing import List

def suggestProducts(products: List[str], searchWord: str):
    products.sort()
    result = []
    prefix = ""
    for char in searchWord:
        prefix += char
        
        # binary search to find the first occurence:
        l, r = 0, len(products) - 1
        while l < r:
            m = (l + r) // 2
            if products[m] < prefix:
                l = m + 1
            else:
                r = m
        
        result.append([products[i] for i in range(l, min(l + 3, len(products))) if products[i].startswith(prefix)])
    return result
    