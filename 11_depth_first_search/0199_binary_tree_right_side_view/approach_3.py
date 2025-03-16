from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode):
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
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
root.right = TreeNode(3)
rightSideView(root)