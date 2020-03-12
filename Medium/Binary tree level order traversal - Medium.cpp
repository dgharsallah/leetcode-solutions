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
    
    map<int, vector<int>> m;
    
    void traverse(TreeNode* root, int depth) {
        if (!root) return;
        m[depth].push_back(root->val);
        // printf("pushing %d at %d\n", root->val, depth);
        if (root->left != NULL) 
            traverse(root->left, depth + 1);
        if (root->right != NULL) 
            traverse(root->right, depth + 1);
    }
    
    vector<vector<int>> levelOrder(TreeNode* root) {
        traverse(root, 0);
        vector<vector<int> > ans;
        for (auto p : m) {
            ans.push_back(p.second);
        }
        return ans;
    }
};
