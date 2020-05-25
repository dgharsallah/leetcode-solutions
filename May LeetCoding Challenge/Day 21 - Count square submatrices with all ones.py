class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        if n == 1:
            res = 0
            for e in matrix:
                res += 1 if e > 0 else 0
            return res
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if i and j:
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j]
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                res += dp[i][j]
        return res
