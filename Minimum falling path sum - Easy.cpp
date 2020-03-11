class Solution {
public:

    int minFallingPathSum(vector<vector<int>>& A) {
        int n = A.size();
        vector<vector<int> > dp(n, vector(n, 0));
        for (int i = 0; i < n; ++i) {
            dp[0][i] = A[0][i];
        }
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
               dp[i][j] = dp[i - 1][j] + A[i][j];
               if (j - 1 >= 0) {
                   dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + A[i][j]);
               }
               if (j + 1 < n) {
                   dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + A[i][j]);
               }
            }
        }
        int ans = 1e9;
        for (int i = 0; i < n; ++i) {
            ans = min(ans, dp[n - 1][i]);
        }
        return ans;
    }
};
