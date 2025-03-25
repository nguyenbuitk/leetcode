from utils import *

def characterReplacement(s: str, k: int) -> int:
    left = 0
    res = 0
    frequence = {}
    for right in range(len(s)):
        print_list_with_indexes(s, l=left, r=right)
        frequence[s[right]] = frequence.get(s[right], 0) + 1
        
        # Expanding the window, if max(frequence) + k >= window_size
        if max(frequence.values()) + k >= right - left + 1:
            res = max(res, right - left + 1)
            continue
        
        # Shrink the window
        else:
            while max(frequence.values()) + k < right - left + 1:
                frequence[s[left]] -= 1
                left += 1
                print_list_with_indexes(s, l=left, r=right)
    return res
print(characterReplacement("AABABBA", 1))