class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        i = 0
        res = 0
        while 1 << i <= N:
            res += 1 << i if (1 << i) & N == 0 else 0
            i += 1
        return res
