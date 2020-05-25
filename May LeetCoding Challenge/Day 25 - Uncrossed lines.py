class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def go(i, j):
            if i == len(A) or j == len(B):
                return 0
            ret = 0
            if A[i] == B[j]:
                ret = go(i + 1, j + 1) + 1
            ret = max(ret, go(i + 1, j))
            ret = max(ret, go(i, j + 1))
            return ret
        
        return go(0, 0)
