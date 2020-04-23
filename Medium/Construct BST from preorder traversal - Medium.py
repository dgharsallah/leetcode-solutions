# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    
        # construct tree starting from ith position
        def getBST(i, low, up):
            if i == len(preorder):
                return None
            cur = preorder[i]
            if cur < low or up < cur:
                return getBST(i + 1, low, up)
            root = TreeNode(cur)
            root.left = getBST(i + 1, low, cur)
            root.right = getBST(i + 1, cur, up)
            return root
        
        if preorder is None:
            return None
        if len(preorder) == 0:
            return None
        
        return getBST(0, -1e9, 1e9)
