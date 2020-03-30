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
    
    int sum[10007], depth = 0;
    
    void dfs(TreeNode* root, int d) {
        if (root == NULL) return;
        sum[d] += root->val;
        depth = max(depth, d);
        if (root->left != NULL)
            dfs(root->left, d + 1);
        if (root->right != NULL)
            dfs(root->right, d + 1);
    }
    
    int maxLevelSum(TreeNode* root) {
        dfs(root, 1);
        int maxSum = -2e9, at;
        for (int i = 1; i <= depth; ++i)
            if (maxSum < sum[i]) {
                maxSum = sum[i];
                at = i;
            }
        return at;
    }
};
