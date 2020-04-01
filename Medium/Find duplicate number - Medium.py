class Solution:
    # Binary search the answer
    def findDuplicate(self, nums: List[int]) -> int:
        l, h, m = 0, len(nums) - 1, len(nums) >> 1
        while l <= h:
            if sum(1 for i in nums if i <= m) > m:
                h = m - 1
            else:
                l = m + 1
            m = (h + l) >> 1
        return m + 1
    # Floyd's cycle detection algorithm
    def findDuplicate(self, nums: List[int]) -> int:
        hare = nums[0]
        tortoise = nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if nums[hare] == nums[tortoise]:
                break
        hare = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return tortoise
        
