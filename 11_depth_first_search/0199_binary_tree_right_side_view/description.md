# Medium
## 199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

# Key Idea
## Approach 1 - BFS (Optimal)
1. Initialize a queue and start level-order traversal
2. At each levle, track the rightmost node
3. At the end of each level, add the last node of that level to the result
```python
    if not root:
        return 
    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(node.val)
    return res
```
**`Time: O(n) Space: O(w)`**

## Approach 2 - DFS (Recursive)
1. Use DFS (preorder traversal) starting from the root
2. At each level, add the first encounter node to the result
3. Recur for the right child first, then the left child
**`Time: O(n) Space: O(h)`**
```python
    if not root:
        return []
    stack, res = [], []
    curr, level = root, 0
    while curr or stack:
        while curr:
            if level >= len(res):
                res.append(curr.val)
            stack.append((curr, level))
            curr, level = curr.right, level + 1

        curr, level = stack.pop()
        curr, level = curr.left, level + 1
    print(res)
```

## Approach 3 - DFS (Stack Iterative)
1. Use a stack (`LIFO`) to perform iterative DFS
    - `stack = [(curr, current_level)]`
2. Track the first node encountered at each depth
3. Process the right child first 
**`Time: O(n) Space: O(h)`**
```python
    res = []
    def dfs(curr, res, currDepth):
        if not curr:
            return
        if currDepth == len(res):
            res.append(curr.val)
        dfs(curr.right, res, currDepth + 1)
        dfs(curr.left, res, currDepth + 1)

    dfs(root, res, 0)
    return res
```

