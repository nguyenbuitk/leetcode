# Medium
### **Problem Statement**
Given a string `s` and an integer `k`, you can replace **at most** `k` characters in `s` with any other uppercase English character.  
Return the **length of the longest substring** that contains the **same letter** after performing the allowed operations.

---

```
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.t.
```

# Key Idea
## Approach 1: Sliding Window (Two Pointers)

1. **Use Two Pointers (`left` and `right`)**
    - The `right` pointer expands the window to include new elements.
    - The `left` pointer shrink the window when more than `k` replacements are needed.
2. **Adjust the window**
    - If more than `k` replacements are needed (`(right - left + 1) - max_freq > k`), shrink the window by moving `left` to the right.
    - Reduce the frequency count of the leftmost character while shrinking the window.
3. **Track the Maximum Substring Length**
    - The valid substring length is `(right - left + 1)`, and we update the `max_length` accordingly.

```python
def characterReplacement(s: str, k: int) -> int:
    left = 0
    res = 0
    frequence = {}
    for right in range(len(s)):

        frequence[s[right]] = frequence.get(s[right], 0) + 1
        max_count = max(frequence.values())

        # check whether we need to shrink window
        if max_count + k < right - left + 1:
            frequence[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res
print(characterReplacement("AABABBA", 1))
```

## Approach 2 - Self
Instead of shrink window 1 index at a time, we shrink until we have valid window
```python
def characterReplacement(s: str, k: int) -> int:
    left = 0
    res = 0
    frequence = {}
    for right in range(len(s)):
        frequence[s[right]] = frequence.get(s[right], 0) + 1
        
        # Expanding the window, if max(frequence) + k >= window_size
        if max(frequence.values()) + k >= right - left + 1:
            res = max(res, right - left + 1)
            continue
        
        # Shrink the window
        else:
            while max(frequence.values()) + k < right - left + 1:
                frequence[s[left]] -= 1
                left += 1
    return res
print(characterReplacement("AABABBA", 1))
```

## Notes.
This problem follows two following rules, than it can apply the `sliding window `
1. If a wider window is valid, the narrow of that wider scope is valid ()
    - Means if `AABA` is valid substring, then `AAB` or `ABA` is valid
2. If a narrower window is invalid, the wider scope of that narrow scoe is invalid
    - Means if `BAB` is invalid, `ABAB` or `BABB` is invalid