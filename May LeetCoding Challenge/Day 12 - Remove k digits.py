class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for c in num:
            while len(s) > 0 and s[-1] > c and k:
                s.pop()
                k -= 1
            s.append(c)
        s = s[:-k] if k > 0 else s
        return "".join(s).lstrip('0') or '0'
