# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        xParent, yParent = None, None
        xDepth, yDepth = 0, 0
        
        def dfs(root, parent, depth):
            nonlocal xParent, yParent, xDepth, yDepth
            if root is None:
                return
            if root.val == x:
                xParent = parent
                xDepth = depth
            if root.val == y:
                yParent = parent
                yDepth = depth
            if root.left is not None:
                dfs(root.left, root, depth + 1)
            if root.right is not None:
                dfs(root.right, root, depth + 1)
        
        dfs(root, None, 0)
        if xParent != yParent and xDepth == yDepth:
            return True
        return False
