from utils import *

def connect(root: Node) -> Node:
    if not root: 
        return root
    # process level 1
    # Problem with not perfect tree: 
    head = root
    while head:
        dummy = Node()
        set_dummy = False
        curr = Node()
        leftmost = head
        while leftmost: # left not always exits
            print(f"head: {head.val} leftmost: {leftmost.val}")
            if leftmost.left:
                curr.next = leftmost.left
                if not set_dummy:
                    dummy = leftmost.left
                    set_dummy= True
                curr = curr.next
            if leftmost.right:
                curr.next = leftmost.right
                if not set_dummy:
                    dummy = leftmost.right
                    set_dummy = True
                curr = leftmost.right
                
            leftmost = leftmost.next
            time.sleep(0.5)
        if not set_dummy:
            return root
        head = dummy
        print(f"head end: {head.val}")
    return root

root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3)
root.right.right = Node(7)
connect(root)
print(root.left.left.next.val)