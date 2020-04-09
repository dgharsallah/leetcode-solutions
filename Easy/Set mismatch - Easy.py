class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        dup = 0
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1
        missing = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]
