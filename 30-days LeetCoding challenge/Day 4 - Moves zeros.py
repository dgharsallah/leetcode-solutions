class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 1
        i = 0
        while i < len(nums):
            if i >= r:
                break
            if nums[i] == 0:
                while 0 <= r and nums[r] == 0:
                    r -= 1
                for j in range(i, r):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                i += 1
        return nums
