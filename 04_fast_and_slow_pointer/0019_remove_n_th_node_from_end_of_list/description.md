# Medium
## 19. Remove Nth Node From End of List
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
```
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
![visualize](../images/remove_ex1.jpg)
```
Example 2:
Input: head = [1], n = 1
Output: []
```

# Key Idea
## Approach 1 (normal)
Notes: this approach will traverse the linked list twice, therefore don't satisfy the requirement (one pass)
- Caculate the length of the linked list
- Remove the nth element based on length

## Approach 2 (fast and slow pointer)
- Move fast pointer `n` steps to create space between fast and slow
- Move both fast and slow pointer when fast is None, at this point, slow pointer is a node needed to be remove