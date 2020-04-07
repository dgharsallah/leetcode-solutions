class Solution:
    def countElements(self, arr: List[int]) -> int:
        f = {}
        for e in arr:
            if f.get(e) == None:
                f[e] = 1
            else:
                f[e] += 1
        ans = 0
        for e in arr:
            if f.get(e + 1) != None and f[e + 1] > 0:
                ans += 1
        return ans
