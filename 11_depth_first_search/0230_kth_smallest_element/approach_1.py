from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def kthSmallest(root: TreeNode, k: int):
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

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print(kthSmallest(root, 6))
