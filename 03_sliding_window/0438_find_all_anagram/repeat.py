from utils import *

def findAnagrams(s: str, p: str) -> int:
    left = 0
    res = []
    frequence = {}
    count_p = Counter(p)
    
    for right in range(len(s)):
        print_list_with_indexes(s, l=left, r=right)
        frequence[s[right]] = frequence.get(s[right], 0) + 1
        print(f"frequence: {frequence}")
        if frequence == count_p:
            res.append(left)
            print(f"res append {left}")
        if right - left + 1  >= len(p):
            frequence[s[left]] -= 1
            if frequence[s[left]] == 0:
                frequence.pop(s[left])
            left += 1
    return res

print(findAnagrams("cbaebabacd", "abc"))