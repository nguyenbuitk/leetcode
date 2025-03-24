from utils import *

def removeNonAlphanumeric(s: str):
    res = []
    for char in s:
        if char.lower().isalnum():
            res.append(char.lower())
    return "".join(res)
            

def isPalindrome(s: str) -> bool:
    s = removeNonAlphanumeric(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True    
    

print(isPalindrome("Hello 324231 dsf!2"))