# Medium
## 129. Sum Root to Leaf Numbers
You are given the `root` of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.


Example 1:\
Input: root = `[1,2,3]`\
Output: `25`\
Explanation:\
The root-to-leaf path `1->2` represents the number `12`.\
The root-to-leaf path `1->3` represents the number `13`.\
Therefore, sum = `12 + 13 = 25`.\
![image](../images/tree1.jpg)

# Key Idea
## Approach 1 - DFS recursive
As we move down, we multiply the sum by 10 and add the current node’s value.\
**`Time O(n), Space O(h)`**
```python
def sumNumbers(root: TreeNode):
    res = []
    def dfs(node, sum):
        if not node:
            return
        sum = sum*10 + node.val
        if not node.left and not node.right:
            res.append(sum)
        else:
            dfs(node.left, sum)
            dfs(node.right, sum)
    
    dfs(root, 0)
    return sum(res)
```
## Approach 2 - DFS iterative (stack)
Use a stack to simulate recursion and track `node, current_number`
```python
    if not root: 
        return 0
    stack = [(root, root.val)] # node, current_val
    res = 0
    while stack:
        node, val = stack.pop()
        if not node.left and not node.right:
            res = res + val
        if node.left:
            stack.append((node.left, val*10 + node.left.val))
        if node.right:
            stack.append((node.right, val*10 + node.right.val))
    return res
```

## Approach 3 - BFS (queue)
Use a queue for level_order traversal, track `node, current_number`
```python
def sumNumbers(root: TreeNode):
    if not root:
        return 0
    res = 0
    queue = deque([(root, 0)])
    while queue:
        node, preVal = queue.popleft()
        current_val = preVal*10 + node.val
        if not node.left and not node.right:
            res += current_val
        if node.left:
            queue.append((node.left, current_val))
        if node.right:
            queue.append((node.right, current_val))
    return res
```