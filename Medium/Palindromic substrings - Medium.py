class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1 
                l -= 1
                r += 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
