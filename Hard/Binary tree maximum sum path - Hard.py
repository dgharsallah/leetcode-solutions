# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.dp = {}
        
        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            max_sum = max(max_sum, root.val + left + right)
            return root.val + max(left, right)
        
        max_sum = -1e9
        dfs(root)
        return max_sum
