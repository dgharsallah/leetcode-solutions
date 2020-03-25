class Solution {
public:
    
    int n, m, ans, dp[101][101];
    
    int go(int i, int j) {
        if (i >= n || j >= m) return 0;
        if (i == n - 1 && j == m - 1) return 1;
        int &ret = dp[i][j];
        if (ret != -1) return ret;
        ret = 0;
        ret += go(i + 1, j);
        ret += go(i, j + 1);
        return ret;
    }
    
    int uniquePaths(int m, int n) {
        this->m = m;
        this->n = n;
        memset(dp, -1, sizeof dp);
        return go(0, 0);
    }
};
