class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    stack, res = [], []
    curr, level = root, 0
    while curr or stack:
        while curr:
            print(f"current node: {curr.val}")
            print(f"current level: {level}")
            if level >= len(res):
                res.append(curr.val)
            stack.append((curr, level))
            curr, level = curr.right, level + 1

        curr, level = stack.pop()
        print(f"current node after poped: {curr.val}")
        print(f"current level after poped: {level}")
        curr, level = curr.left, level + 1
    print(res)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
rightSideView(root)
