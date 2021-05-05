class Solution:
    
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize = None) 
        def go(i):
            if i >= len(nums) - 1:
                return 0
            ret = 1e9
            for j in range(1, nums[i] + 1):
                ret = min(ret, go(i + j) + 1)
            return ret
    
        return go(0)
