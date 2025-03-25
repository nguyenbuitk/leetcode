from utils import *

def findDuplicate(nums):
    dict = Counter(nums)
    for key, val in dict.items():
        if val > 1:
            return key
    
findDuplicate([3,1,4,3,2])    