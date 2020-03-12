class Solution {
public:
    bool vis[10001] = {0};
    
    int countChildren(int u, vector<int>& leftChild, vector<int>& rightChild) {
        if (u == -1) return 0;
        if (vis[u]) return -1e5;
        vis[u] = true;
        int l = countChildren(leftChild[u], leftChild, rightChild);
        int r = countChildren(rightChild[u], leftChild, rightChild);
        return l + r + 1;
    }
    
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        int deg[10001] = {0};
        for (int i = 0; i < n; ++i) {
            if (leftChild[i] != -1) deg[leftChild[i]]++;
            if (rightChild[i] != -1) deg[rightChild[i]]++;
        }
        int total = 0;
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 0) {
                total = countChildren(i, leftChild, rightChild);
                break;
            }
        }
        return total == n;
    }
};
