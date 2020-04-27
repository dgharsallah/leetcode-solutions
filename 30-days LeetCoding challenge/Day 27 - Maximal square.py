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
