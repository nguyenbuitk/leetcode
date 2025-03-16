from typing import Optional, List

def postorderTraversal(self, root) -> List[int]:
    return self.preorderTraversal(root.left) + self.preorderTraversal(root.right)  + [root.val] if root else []

def postorderTraversal(root):
    res = []
    def dfs(root):
        if not root:
            return
        
        dfs(root.left)
        dfs(root.right)
        res.append(root.val)

    return res

