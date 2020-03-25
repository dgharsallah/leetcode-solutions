class Solution {
public:
    
    int n, m, ans, dp[101][101];
    vector<vector<int> > g;
    
    int go(int i, int j) {
        if (i >= n || j >= m || g[i][j] == 1) return 0;
        if (i == n - 1 && j == m - 1) return 1;
        int &ret = dp[i][j];
        if (ret != -1) return ret;
        ret = 0;
        ret += go(i + 1, j);
        ret += go(i, j + 1);
        return ret;
    }
    
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        this->m = obstacleGrid[0].size();
        this->n = obstacleGrid.size();
        this->g = obstacleGrid;
        memset(dp, -1, sizeof dp);
        return go(0, 0);
    }
};
