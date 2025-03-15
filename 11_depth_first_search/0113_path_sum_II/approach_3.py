from utils import *


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root: 
        return []
    res = []
    queue = deque([(root, [root.val], root.val)])
    while queue:
        curr_node, path, sum = queue.popleft()
        print(f"\ncurr_node: {curr_node.val}")
        print(f"id_path: {id(path)} path: {path}")
        if not curr_node.left and not curr_node.right and sum == targetSum:
            res.append(path)
        if curr_node.left:
            queue.append((curr_node.left, path + [curr_node.left.val], sum + curr_node.left.val))
        if curr_node.right:
            queue.append((curr_node.right, path + [curr_node.right.val], sum + curr_node.right.val))
            
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
print(pathSum(root, 22))
