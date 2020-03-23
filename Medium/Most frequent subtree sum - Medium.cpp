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
    
    map<int, int> f;
    
    int dfs(TreeNode* root) {
        if (root == NULL) return 0;
        int res = root->val;
        if (root->left != NULL)
            res += dfs(root->left);
        if (root->right != NULL)
            res += dfs(root->right);
        f[res]++;
        return res;
    }
    
    vector<int> findFrequentTreeSum(TreeNode* root) {
        dfs(root);
        vector<int> ans;
        int mx = 0;
        for (auto p : f) {
            if (p.second == mx)
                ans.push_back(p.first);
            if (p.second > mx) {
                mx = p.second;
                ans.clear();
                ans.push_back(p.first);
            }
        }
        return ans;
    }
};
