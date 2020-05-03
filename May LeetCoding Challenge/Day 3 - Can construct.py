class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f = {}
        for c in magazine:
            f[c] = f.get(c, 0) + 1
        for c in ransomNote:
            f[c] = f.get(c, 0) - 1
            if f[c] < 0:
                return False
        return True
