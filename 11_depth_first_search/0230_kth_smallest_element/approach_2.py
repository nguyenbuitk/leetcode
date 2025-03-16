from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def kthSmallest(root: TreeNode, k: int):
    # dfs inorder traversal
    order = 1
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(f"current node: {curr.val}, order = {order}")
        if order == k:
            return curr.val
        order += 1
        curr = curr.right

    return False


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print(kthSmallest(root, 6))