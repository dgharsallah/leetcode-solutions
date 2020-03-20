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
    
    void merge(TreeNode* root, TreeNode* &cur) {
        if (root == NULL) return;
        cur->val += root->val;
        if (root->left != NULL) {
            if (cur->left == NULL) cur->left = new TreeNode(0);
            merge(root->left, cur->left);
        }
        if (root->right != NULL) {
            if (cur->right == NULL) cur->right = new TreeNode(0);
            merge(root->right, cur->right);
        }
    }
    
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return NULL;
        TreeNode* res = new TreeNode(0);
        TreeNode* cur = res;
        merge(t1, cur);
        cur = res;
        merge(t2, cur);
        return res;
    }
};
