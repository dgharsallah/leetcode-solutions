class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        dv = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(matrix)
        m = 0 if len(matrix) == 0 else len(matrix[0])
        
        @lru_cache(maxsize=None)
        def go(i, j):
            ret = 1
            for v in dv:
                ni = i + v[0]
                nj = j + v[1]
                if 0 <= ni and ni < n and 0 <= nj and nj < m and matrix[ni][nj] > matrix[i][j]:
                    ret = max(ret, go(ni, nj) + 1)
            return ret
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, go(i, j))
        return res
