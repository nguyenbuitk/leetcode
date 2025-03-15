from utils import *

def connect(root: Node) -> Node:
    if not root:
        return
    
    queue = deque([root])
    while queue:
        level_size = len(queue)
        prev = None
        
        for _ in range(level_size):
            node = queue.popleft()
            if prev:
                prev.next = node
            prev = node
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
    
    return root