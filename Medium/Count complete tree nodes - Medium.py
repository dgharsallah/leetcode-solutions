# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depth = 0
        total_nodes = 0
        cur_node = root
        while cur_node != None:
            cur_node = cur_node.left
            depth += 1
        # all nodes expect last layer
        total_nodes = (1 << (depth - 1)) - 1
        l = 0
        r = (1 << depth - 1) - 1
        mid = 0
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            cur_node = root
            i = depth - 2
            while i >= 0:
                if (1 << i) & mid == 0:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
                i -= 1
            check = cur_node != None
            if check:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        total_nodes += ans + 1
        return total_nodes
