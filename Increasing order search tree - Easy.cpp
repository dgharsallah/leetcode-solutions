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
    
    void traverse_inorder(TreeNode* root, TreeNode* &cur) {
        if (root->left != NULL) {
            traverse_inorder(root->left, cur);
        }
        cur->left = NULL;
        cur->right = new TreeNode(root->val);
        cur = cur->right;
        if (root->right != NULL) {
            traverse_inorder(root->right, cur);
        }
    }

    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* res = new TreeNode(0);
        TreeNode* cur = res;
        traverse_inorder(root, cur);
        return res->right;
    }
};
