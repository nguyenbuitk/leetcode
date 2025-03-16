from utils import *

def connect(root: Node) -> Node:
    if not root:
        return
    
    head = root
    while head:
        dummy = Node(0) # Dummy node to track the start of the next level. Unlike perfect tree, where we always can get leftmost node of next level, but in this tree, we must create dummy to track the first node of next level. When we process next level, we will start at this pointer
        curr = dummy    # Point to construct next level
        temp = head     # Iterate current level
        print(f"\ndummy: {dummy.val}\ncurr: {curr.val}, temp: {temp.val}")
        while temp:     # current level
            if temp.left:
                curr.next = temp.left
                curr = curr.next
            if temp.right:
                curr.next = temp.right
                curr = curr.next
            temp = temp.next
        
        head = dummy.next
        print(f"{id(dummy)}")
        print(f"{id(curr)}")
        print(f"end head = {head.val if head else ''}")
    return root

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3)
root.right.right = Node(7)
connect(root)