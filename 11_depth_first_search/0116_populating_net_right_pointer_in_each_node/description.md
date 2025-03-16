# Medium
## 116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.\
Example 1
![visualize](../images/116_sample.png)

# Key Idea

## Approach 1 - BFS self
### [Script Link](./approach_1.py)
1. Perform level order traveral.
2. At each level, link nodes from **left to right** using `next`
3. Ensure last node at each level point to `None`
<br />
<br />

## Approach 2 - BFS optimize (chatgpt)
**`O(n) time, O(n) space`**
### [Script Link](./approach_2.py)
Similar idea with approach 1, but clean up
<br />
<br />

## Approach 3 - DFS Recursive
### [Script Link](./approach_3.py)
**`O(n) time, O(logn) space`**
```python
def connect(root: Optional[Node]):
    if not root or not root.left:
        return root
    print(f"current: {root.val}")
    
    # Connect the left child to right child of current node
    root.left.next = root.right
    
    # Connect the right child to next node's left child (if exists)
    if root.next:
        root.right.next = root.next.left
        
    # Recursive call for left and right subtrees
    connect(root.left)
    connect(root.right)
```
<br />
<br />

## Approach 4 - BFS more optimized
### [Script link and debug](./approach_4.py)
**`O(n) time, O(1) space`**
```python
    if not root:
        return None

    leftmost = root
    while leftmost.left: # check children exits
        # Start from the root
        curr = leftmost
        
        # Iterative current level from root
        while curr:
            # Connect left child to right child
            curr.left.next = curr.right

            # Connect right child to the next node's left child
            if curr.next:
                curr.right.next = curr.next.left

            # Move to next node in the same level
            curr = curr.next

        # Move to next level
        leftmost = leftmost.left 
    return root
```

