class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        n = len(matrix)
        m = 0 if len(matrix) == 0 else len(matrix[0])
        cur_row = [0 for _ in range(m + 1)]
        prev_row = [0 for _ in range(m + 1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    cur_row[j + 1] = min(prev_row[j + 1], min(prev_row[j], cur_row[j])) + 1
                else:
                    cur_row[j + 1] = 0
                ans = max(ans, cur_row[j + 1])
            prev_row = copy.deepcopy(cur_row)
        return ans * ans
      
      def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        n = len(matrix)
        m = 0 if len(matrix) == 0 else len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                cur_cell = 1 if matrix[i][j] == '1' else 0
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j + 1], min(dp[i][j], dp[i + 1][j])) + 1
                else:
                    dp[i + 1][j + 1] = 0
                ans = max(ans, dp[i + 1][j + 1])
        return ans * ans
      
      def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        n = len(matrix)
        m = 0 if len(matrix) == 0 else len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = 1 if matrix[i][j] == '1' else 0
                ans = max(ans, dp[i][j])
                if i != 0:
                    dp[i][j] += dp[i - 1][j]
                if j != 0:
                    dp[i][j] += dp[i][j - 1]
                if i > 0 and j > 0:
                    dp[i][j] -= dp[i - 1][j - 1]
                l = min(i, j)
                for k in range(l + 1):
                    rem = 0
                    si = i - k
                    sj = j - k
                    if si > 0:
                        rem = dp[si - 1][j]
                    if sj > 0:
                        rem += dp[i][sj - 1]
                    if si > 0 and sj > 0:
                        rem -= dp[si - 1][sj - 1]
                    sz = (j - sj + 1) * (i - si + 1)
                    if dp[i][j] - rem == sz:
                        ans = max(ans, sz)
        return ans
