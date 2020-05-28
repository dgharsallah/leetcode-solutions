class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i // 2] + (i % 2))
        return ans
