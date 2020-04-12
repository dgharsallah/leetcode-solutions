# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    d = {}
    
    def dfs1(self, root: TreeNode):
        if root == None:
            return 0
        l = 0
        r = 0
        if root.left != None:
            l = self.dfs1(root.left) + 1
        if root.right != None:
            r = self.dfs1(root.right) + 1
        self.d[root] = max(l, r)
        return self.d[root]
    
    def dfs2(self, root:TreeNode):
        if root == None:
            return
        cur = 0
        l = 0
        r = 0
        if root.left != None:
            cur += self.d[root.left] + 1
            l = self.dfs2(root.left)
        if root.right != None:
            cur += self.d[root.right] + 1
            r = self.dfs2(root.right)
        return max(l, max(r, cur))
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.dfs1(root)
        return self.dfs2(root)
