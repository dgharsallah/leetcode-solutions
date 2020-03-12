class Solution {
public:
    
    map<int, vector<int>> m;
    
    void traverse(TreeNode* root, int depth) {
        if (!root) return;
        m[depth].push_back(root->val);
        if (root->left != NULL) 
            traverse(root->left, depth + 1);
        if (root->right != NULL) 
            traverse(root->right, depth + 1);
    }
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        traverse(root, 0);
        vector<vector<int> > ans;
        for (auto p : m) {
            ans.push_back(p.second);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
