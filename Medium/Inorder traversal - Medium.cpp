// *
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };

class Solution {
public:
    
    // Recursive solution
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root) {
            return vector<int>();
        }
       vector<int> ans;
       if (root->left != NULL) {
           vector<int> l = inorderTraversal(root->left);
           ans.insert(ans.end(), l.begin(), l.end());
       }
        ans.push_back(root->val);
        if (root->right != NULL) {
            vector<int> r = inorderTraversal(root->right);
            ans.insert(ans.end(), r.begin(), r.end());
        }
        return ans;
    }
    
    // Iterative solution
    vector<int> inorderTraversal(TreeNode* root) {
      if (!root) {
          return vector<int>();
      }
      vector<int> ans;
      stack<TreeNode*> s;
      s.push(root);
      while(!s.empty()) {
          TreeNode* cur = s.top();
          if (cur->left == NULL) {
              ans.push_back(cur->val);
              TreeNode* tmp = cur->right;
              s.pop();
              if (tmp != NULL) {
                  s.push(tmp);
              }
          } else {
              s.push(cur->left);
              cur->left = NULL;
          }
      }
      return ans;
    }
};
