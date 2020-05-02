class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        is_jewel = {}
        for j in J:
            is_jewel[j] = True
        ans = 0
        for s in S:
            if is_jewel.get(s, False):
                ans += 1
        return ans
