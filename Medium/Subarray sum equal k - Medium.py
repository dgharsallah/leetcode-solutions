class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f = {}
        f[0] = 1
        cs = 0
        ans = 0
        for e in nums:
            cs += e
            if f.get(cs - k) != None:
                ans += f[cs - k]
            if f.get(cs) == None:
                f[cs] = 1
            else:
                f[cs] += 1
        return ans
