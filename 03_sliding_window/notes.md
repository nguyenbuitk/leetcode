# Summary of what kind of problem can/ cannot solved by Two Pointers
[Link origial](https://leetcode.com/problems/subarray-sum-equals-k/solutions/301242/general-summary-of-what-kind-of-problem-can-cannot-solved-by-two-pointers/)

## When can we use "Two pointer" or "Sliding windows"
**When two pointer come into place to help us reduce the total cases we need to consider, such that the corresponding time complexity will reduce too**
This summary is simple

`1. If a wider window is valid, the narrow of that wider scope is valid`

`2. If a narrower window is invalid, the wider scope of that narrow scope is invalid`

## Explaination

The problem requires finding the longest substring without repeating characters [Problem 3 leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/). To resolve this, we could use **Sliding Window** with two pointers `i` and `j`, where
- `i` is a starting point of the window
- `j` is a end point of the window

**If a wider window is valid, then any narrower window within it also valid**
- Meaning: if substring `[i:j]` contains no repeating characters, then any substring with in `[i:j]` also contains no repeating character
```
e.g
Input: "abcabcbb"
When considering the window "abc", it's valid because no duplicate characters. If narrow the window "ab", it is still valid beacuse no duplicate character
```

**If a narrower window is invalid, the wider scope of that narrow scope is invalid**
- Meaning: If a substring `[i:j]` is not valid (contian duplicate character), then any substring extend from it will also be invalid
```
e.g
Input: "abcabcbb"
When considering the window "abca", it is invalid. when extend the window to "abcab", it is still not valid cause the character `a` still duplicate
```

Why two characteristic help us solve the problem with **Sliding Window**
- Once a valid window is found, we can expand `j` to find a larger valid window
- If the window is not valid, we move `i` to the right to make it valid again
- No need to re-examine the known invalid cases, making the algorithm more optimal
