from utils import *

def connect(root: Optional[Node]):
    if not root or not root.left:
        return root
    print(f"current: {root.val}")
    
    # Connect the left child to right child of current node
    root.left.next = root.right
    
    # Connect the right child to next node's left child (if exists)
    if root.next:
        root.right.next = root.next.left
        
    # Recursive call for left and right subtrees
    connect(root.left)
    connect(root.right)
    

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))
connect(root)
print(root.left.next.val)
    