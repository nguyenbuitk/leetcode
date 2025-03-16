from utils import *

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
        
    
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)

root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print(sumNumbers(root))
