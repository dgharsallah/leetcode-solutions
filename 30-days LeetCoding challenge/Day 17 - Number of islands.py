class Solution:
    
    def numIslands(self, grid) -> int:
    
        vis = []
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n = 0
        m = 0

        def dfs(i, j):
            vis[i][j] = True
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue
                if not vis[ni][nj] and grid[ni][nj] == '1':
                    dfs(ni, nj)
                    
        n = len(grid)
        m = len(grid[0]) if len(grid) > 0 else 0
        vis = [[False for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
