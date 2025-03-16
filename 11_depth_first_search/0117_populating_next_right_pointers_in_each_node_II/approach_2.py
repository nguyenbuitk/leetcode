from utils import *

def connect(root: Optional[Node]):
    if not root:
        return root
    print(f"\ncurrent root: {root.val}")
    
    # Connect the left child to right child of current node
    head = root
    dummy = Node(0)
    if root.left.next:
        root.lef
    while head:
        print(f"current head {head.val}")
        dummy = Node(0)
        curr = dummy
        if head.left:
            print(f"{curr.val}.next = {head.left.val}")
            curr.next = head.left
            curr = curr.next
        
        # Connect the right child to next node's left child (if exists)
        if head.right:
            curr.next = head.right
            curr = curr.next
            
        head = head.next
    # Recursive call for left and right subtrees
    connect(root.left)
    connect(root.right)
    return root

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3)
root.right.right = Node(7)
connect(root)
print(root.left.left.next.next.val)
