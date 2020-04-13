class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cs = [0]
        for i in range(len(nums)):
            cs.append(cs[i] + (-1 if nums[i] == 0 else 1))
        hm = {0: 0}
        ans = 0
        for i in range(len(nums)):
            if hm.get(cs[i + 1]) != None:
                ans = max(ans, i + 1 - hm.get(cs[i + 1]))
            else:
                hm[cs[i + 1]] = i + 1
        return ans
