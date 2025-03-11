class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        l, r = 0, 0
        n = len(s)
        dict = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        while r < n:
            while min(dict.values()) < 1 and r < n:
                dict[s[r]] += 1
                r += 1

            if min(dict.values()) >= 1:
                count += n - r + 1
            dict[s[l]] -= 1
            l += 1
            while min(dict.values()) >= 1:
                count += n - r + 1
                dict[s[l]] -= 1
                l += 1
        return count