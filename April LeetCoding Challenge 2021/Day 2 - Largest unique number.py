class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        f = [0] * 1001
        for e in A:
            f[e] += 1
        ans = -1
        for idx, val in enumerate(f):
            if val == 1:
                ans = max(ans, idx)
        return ans
