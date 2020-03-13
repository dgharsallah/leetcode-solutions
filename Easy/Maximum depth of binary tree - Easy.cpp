/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    int dfs(TreeNode* root) {
        if (root == NULL) return 0;
        int l = 0, r = 0;
        if (root->left != NULL)
            l = dfs(root->left) + 1;
        if (root->right != NULL)
            r = dfs(root->right) + 1;
        return max(l, r);
    }
    
    int maxDepth(TreeNode* root) {
        return dfs(root) + (root != NULL);
    }
};
