from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
def connect(node: Node):
    if not node:
        return None
    queue = deque([node])
    while queue:
        level_size = len(queue)         # number of nodes at current level
        preNode = queue.popleft()       # process the first node of current level
        
        # If it has children, enqueue both left and right (perfect binary tree)
        if preNode.left:                
            queue.append(preNode.left)
            queue.append(preNode.right)
            
        # Process remaining node in the level
        for _ in range(1, level_size):
            node = queue.popleft()      # get next node in the level
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
            # connect previous node to current node
            preNode.next = node
            preNode = node
            
        # The last node in the level should point to NULL
        preNode.next = None

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))
connect(root)
print(root.left.left.next.next.next.val)


