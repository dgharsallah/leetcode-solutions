# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def invert(self, root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        if root.left != None:
            self.invert(root.left)
        if root.right != None:
            self.invert(root.right)
        
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
