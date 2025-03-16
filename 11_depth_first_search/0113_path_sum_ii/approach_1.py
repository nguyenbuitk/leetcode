class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int):
    res = []
    def dfs(node, path, running_sum):
        if not node:
            return
        print(f"current node: {node.val}")
        print(f"current path: {path}")
        print(f"reference of path: {id(path)}", end="\n")
        
        path.append(node.val)
        running_sum += node.val
        if not node.left and not node.right and running_sum == targetSum:
            res.append(path[:])

        dfs(node.left, path, running_sum)
        dfs(node.right, path, running_sum)

        # Backtrack: Remove the last element before returning to previous state
        path.pop()
    dfs(root, [], 0)
    return res

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
pathSum(root, 22)
