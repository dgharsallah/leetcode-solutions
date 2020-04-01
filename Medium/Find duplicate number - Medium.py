class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, h, m = 0, len(nums) - 1, len(nums) >> 1
        while l <= h:
            if sum(1 for i in nums if i <= m) > m:
                h = m - 1
            else:
                l = m + 1
            m = (h + l) >> 1
        return m + 1
        
        
