from utils import *
def validPalindrome(s: str) -> bool:
    print_list_with_indexes(s)
    l, r = 0, len(s) - 1
    while l < r:
        print(f"l, r: {l}, {r}")
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        break
    if l >= r - 1:
        return True

    pl, pr = l, r
    while l + 1 < pr:
        print(f"l + 1, r: {l+1}, {r}")
        if s[l+1] == s[r]:
            l += 1
            r -= 1
            continue
        break
    if l >= r:
        return True

    while pl < pr - 1:
        print(f"pl, pr-1: {pl}, {pr-1}")
        if s[pl] == s[pr - 1]:
            pl += 1
            pr -= 1
            continue
        break
    if pl >= pr - 1:
        return True
    return False
        
print(validPalindrome("aczzcba"))