/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    
    int maxDepth(Node* root) {
        if (root == NULL) {
            return 0;
        }
        int ans = 1;
        for (auto v : root->children) {
            ans = max(ans, maxDepth(v) + 1);
        }
        return ans;
    }
};
