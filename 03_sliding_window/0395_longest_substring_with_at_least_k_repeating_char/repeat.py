from utils import *

def longestSubString(s: str, k: int) -> int:
    if not s:
        return 0
    count = Counter(s)
    
    if max(count.values()) < k:
        return 0
    if min(count.values()) >= k:
        return len(s)
    
    res = []
    for key, val in count.items():
        if val < k:
            list_sub_string = s.split(key)
            print(f"list sub string: {list_sub_string}")
            break
    for str in list_sub_string:
        res.append(longestSubString(str, k))
        
    return max(res)
    
print(longestSubString("bbaaacbd", 3))
    