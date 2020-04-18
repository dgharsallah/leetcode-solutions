
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if len(grid) > 0 else 0
        if n == 1 and m == 1:
            return grid[0][0]
        ans = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                up = 1e9
                left = 1e9
                if i > 0:
                    up = grid[i - 1][j]
                if j > 0:
                    left = grid[i][j - 1]
                grid[i][j] += min(up, left)
                ans = grid[i][j]
        return ans
