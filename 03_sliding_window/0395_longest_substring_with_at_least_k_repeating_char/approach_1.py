class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dict = {}
        for right in s:
            dict[right] = dict.get(right, 0) + 1
        
        # Find character that occurs less than k times
        for right in s:
            if dict[right] < k:
                
                # Split at invalid character and recurse
                res_end = []
                for sub in s.split(right):
                    res_end.append(self.longestSubstring(sub, k))
                return max(res_end)

        # If all characters are valid
        return len(s)
            
            
        
solution = Solution()
print(solution.longestSubstring("ababbc", 2))