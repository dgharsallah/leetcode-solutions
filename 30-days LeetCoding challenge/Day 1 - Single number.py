class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for e in nums:
            a ^= e
        return a
