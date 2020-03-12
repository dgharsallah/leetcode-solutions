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
    void getInorderLeaves(TreeNode* root, vector<int>& v) {
        if (!root) {
            return;
        }
        getInorderLeaves(root->left, v);
        if (!root->right && !root->left) {
            v.push_back(root->val);    
        }
        getInorderLeaves(root->right, v);
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> v1, v2;
        getInorderLeaves(root1, v1);
        getInorderLeaves(root2, v2);
        return v1 == v2;
    }
};
