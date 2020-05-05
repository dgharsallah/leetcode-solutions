class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}
        for i in range(len(s)):
            if f.get(s[i]) is None:
                f[s[i]] = [i]
            else:
                f[s[i]].append(i)
        ans = 1e9
        for k in f:
            if len(f[k]) == 1:
                ans = min(ans, f[k][0])
        return ans if ans != 1e9 else -1
