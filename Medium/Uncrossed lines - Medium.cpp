class Solution {
public:
    
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int n = A.size(), m = B.size();
        vector<vector<int> > dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                dp[i][j] = max(dp[i][j], dp[i][j - 1]);
                if (A[i - 1] == B[j - 1]) 
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
            }
        }
        int ans = 0;
        for (int i = 1; i <= m; ++i) {
            ans = max(ans, dp[n][i]);
        }
        return ans;
    }
};
