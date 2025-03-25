from utils import *

def characterReplacement(s: str, k: int) -> int:
    left = 0
    res = 0
    frequence = {}
    for right in range(len(s)):
        print_list_with_indexes(s, l=left, r=right)
        
        frequence[s[right]] = frequence.get(s[right], 0) + 1
        max_count = max(frequence.values())
        if max_count + k < right - left + 1:
            frequence[s[left]] -= 1
            left += 1
            print_list_with_indexes(s, l=left, r=right)
        res = max(res, right - left + 1)
    return res
print(characterReplacement("AABABBA", 1))