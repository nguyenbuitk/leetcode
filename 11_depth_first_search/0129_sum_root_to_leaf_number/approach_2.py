class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: TreeNode) -> int:
    if not root: 
        return 0
    stack = [(root, root.val)] # node, current_val
    res = 0
    while stack:
        node, val = stack.pop()
        print(f"node: {node.val}, val = {val}")
        if not node.left and not node.right:
            res = res + val
            print(f"val: {val}, res = {res}")
        if node.left:
            stack.append((node.left, val*10 + node.left.val))
        if node.right:
            stack.append((node.right, val*10 + node.right.val))
    return res

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)

root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sumNumbers(root))
