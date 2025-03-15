from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(root: Node):
    if not root:
        return None
    res = root

    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        preNode = None
        for _ in range(level_size):
            node = queue.popleft()
            if preNode:
                preNode.next = node
            print(f"curr node: {node.val}, pre node: {preNode.val if preNode else ''}")
            preNode = node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
    return res
root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(7))
connect(root)
print(root.left.left.next.next.val)
