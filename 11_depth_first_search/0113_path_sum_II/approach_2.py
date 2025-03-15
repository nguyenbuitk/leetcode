from utils import *

def pathSum(root: Optional[TreeNode], sum: int):
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, path = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(path)
        if curr.right:
            stack.append((curr.right, val - curr.right.val, path + [curr.right.val]))
        if curr.left:
            stack.append((curr.left, val - curr.left.val, path + [curr.left.val]))
    return res
            
    