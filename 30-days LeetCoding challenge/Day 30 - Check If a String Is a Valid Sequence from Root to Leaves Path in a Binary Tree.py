# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        def dfs(root, idx):
            if root is None:
                return True if idx == len(arr) else False
            # non leaf and 
            if idx >= len(arr):
                return False
            if root.val == arr[idx]:
                if idx == len(arr) - 1:
                    return True if root.left is None and root.right is None else False
            else:
                return False
            return dfs(root.left, idx + 1) or dfs(root.right, idx + 1)
        
        return dfs(root, 0)
