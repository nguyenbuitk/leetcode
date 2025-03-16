# Medium
## 230. Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```
![visualize](../images/kthtree2.jpg)

# Key Idea
## Approach 1 - DFS Recursive
**Using inorder traversal to get the order of target**\
**`Time O(h), space O(h)`**

```python
    current = 0  # Tracks the number of elements visited
    result = None  # Stores the k-th smallest element
    
    def dfs(node):
        nonlocal current, result
        if not node or result is not None:
            return
        
        # Inorder traversal: Left -> Node -> Right
        dfs(node.left)
        
        current += 1
        if current == k:
            result = node.val
            return
        
        dfs(node.right)
    
    dfs(root)
    return result if result is not None else False
```

## Approach 2 - DFS Iterative (Stack)
**`Time O(h), space O(h)`**
```python
    # dfs inorder traversal
    order = 1
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if order == k:
            return curr.val
        order += 1
        curr = curr.right

    return False
```

## Approach 3 - BFS
**Not ideal**\
**`Time O(nlogn) (due to sort), space O(n)`**
1. Use queue to traveral level order node
2. Sorted the value and then return the `kth` value
