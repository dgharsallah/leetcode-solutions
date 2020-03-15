
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
    
    vector<int> v;
    
    TreeNode* build(int l, int r) {
        if (r < l) return NULL;
        int mid = (l + r) / 2;
        TreeNode* root = new TreeNode(v[mid]);
        root->left = build(l, mid - 1);
        root->right = build(mid + 1, r);
        return root;
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        v = nums;
        TreeNode* root = new TreeNode(0);
        TreeNode* cur = root;
        return build(0, nums.size() - 1);
    }
};
