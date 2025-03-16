from utils import *

def connect(root: Node) -> Node:
    if not root:
        return None

    leftmost = root
    while leftmost.left: # check children exits
        # Start from the root
        curr = leftmost
        
        # Iterative current level from root
        while curr:
            # Process next level
            print(f"\ncurr: {curr.val}, curr.next: {curr.next.val if curr.next else ''}")
            print(f"curr.left.next: {curr.right.val}")
            # 
            curr.left.next = curr.right
            if curr.next:
                print(f"curr.right.next: {curr.next.left.val}")
                curr.right.next = curr.next.left
            curr = curr.next
            time.sleep(0.5)
        leftmost = leftmost.left
    return root
root = Node(1)
root.left = Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11)))
root.right = Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15)))

connect(root)

# Output
"""
curr: 1, curr.next: 
curr.left.next: 3

curr: 2, curr.next: 3
curr.left.next: 5
curr.right.next: 6

curr: 3, curr.next: 
curr.left.next: 7

curr: 4, curr.next: 5
curr.left.next: 9
curr.right.next: 10

curr: 5, curr.next: 6
curr.left.next: 11
curr.right.next: 12

curr: 6, curr.next: 7
curr.left.next: 13
curr.right.next: 14

curr: 7, curr.next: 
curr.left.next: 15
"""