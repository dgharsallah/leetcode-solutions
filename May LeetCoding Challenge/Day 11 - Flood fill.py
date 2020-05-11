class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dv = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(image)
        m = len(image[0]) if n > 0 else 0
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        def is_valid(i, j):
            return 0 <= i and i < n and 0 <= j and j < m
        
        def dfs(i, j):
            vis[i][j] = True
            color = image[i][j]
            image[i][j] = newColor
            for di, dj in dv:
                ni = i + di
                nj = j + dj
                if is_valid(ni, nj) and not vis[ni][nj] and color == image[ni][nj]:
                    dfs(ni, nj)
        
        dfs(sr, sc)
        return image
