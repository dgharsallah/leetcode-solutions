class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        i = 0
        res = 0
        while 1 << i <= num:
            res += 1 << i if (1 << i) & num == 0 else 0
            i += 1
        return res
