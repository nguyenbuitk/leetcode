from utils import *

def lengthOfLongestSubstring(s: str) -> int:
    print_list_with_indexes(s)
    dict = set()
    res = 0
    left = 0
    for right in range(len(s)):
        # expand window
        if s[right] not in dict:
            print(dict)
            dict.add(s[right])
            res = max(res, right - left + 1)

        # narrow window
        else:
            while s[right] in dict:
                dict.remove(s[left])
                left += 1
                print_list_with_indexes(s, l=left, r=right)
            dict.add(s[right])
                
    return res
print(lengthOfLongestSubstring("abcabcbb"))