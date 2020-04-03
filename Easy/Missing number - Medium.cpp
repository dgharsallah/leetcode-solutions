class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        for i in range(len(nums)):
            a ^= i ^ nums[i]
        return a
