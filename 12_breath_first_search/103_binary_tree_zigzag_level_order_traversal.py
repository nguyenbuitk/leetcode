from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    res = []
    zigzag = True
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        if zigzag:
            res.append(current_level)
            zigzag = False
        else:
            current_level.reverse()
            res.append(current_level)
            zigzag = True
    return res
    
    

root = TreeNode(3)
root.left = TreeNode(4, TreeNode(1), TreeNode(2))
root.right = TreeNode(5)
print(zigzagLevelOrder(root))