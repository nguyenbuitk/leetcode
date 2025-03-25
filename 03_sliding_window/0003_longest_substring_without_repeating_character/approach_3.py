from utils import *

def lengthOfLongest(s: str) -> int:
    res = 0 
    dict = {}
    left = 0
    for right in range(len(s)):
        # shrink the window
        if s[right] in dict and dict[s[right]] >= left:        
            left = dict[s[right]] + 1
            dict[s[right]] = right

        else:
            dict[s[right]] = right
        print_list_with_indexes(s, left = left, right = right)
        res = max(res, right - left + 1)
    return res

print(lengthOfLongest("abba"))
        