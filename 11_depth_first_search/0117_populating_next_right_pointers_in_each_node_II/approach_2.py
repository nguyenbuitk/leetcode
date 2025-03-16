from utils import *

def connect(root: Optional[Node]):
    if not root:
        return root
    def findNext(node):
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None
    if root.left:
        if root.right:
            print(f"root.left.next ({root.left.val}.next) = root.right ({root.right.val}) ")
            root.left.next = root.right
        else:
            a = findNext(root.next)
            if a:
                print(f"root.left.next ({root.left.val}.next) = {a.val}")
            root.left.next = a
        
    if root.right:
        a = findNext(root.next)
        if a:
            print(f"root.right.next ({root.right.val}.next) = {a.val}")
        root.right.next = a
    print('\n')
        
    connect(root.left)
    return root

def insert_level_order(arr):
    if not arr:
        return None
    
    from collections import deque
    root = Node(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        curr = queue.popleft()
        
        # Assign left child
        if i < len(arr) and arr[i] is not None:
            curr.left = Node(arr[i])
            queue.append(curr.left)
        i += 1

        # Assign right child
        if i < len(arr) and arr[i] is not None:
            curr.right = Node(arr[i])
            queue.append(curr.right)
        i += 1

    return root


# Given list
# arr = [1,2,3,4,5,None,7,None,None,None,8,None,9]
arr = [2,1,3,0,7,9,1,2,None,1,0,None,None,8,8,None,None,None,None,7]

# Construct tree
root = insert_level_order(arr)
connect(root)
# print(root.left.left.left.next.next.next.val)
# printEachNexLevel(root)
