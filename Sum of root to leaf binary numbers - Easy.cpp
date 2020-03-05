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
    
    int dfs(TreeNode* root, string buff) {
        buff += char(root->val + '0');
        if (root->left == NULL && root->right == NULL) {
            reverse(buff.begin(), buff.end());
            int res = 0;
            for (int i = 0; i < buff.size(); ++i) {
                res += (buff[i] - '0') * (1 << i);
            }
            return res;
        }
        int left = 0, right = 0;
        if (root->left != NULL) {
            left = dfs(root->left, buff);
        }
        if (root->right != NULL) {
            right = dfs(root->right, buff);
        }
        return left + right;
    }
    
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, "");
    }
};  
