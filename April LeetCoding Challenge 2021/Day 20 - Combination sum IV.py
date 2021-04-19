class Solution:
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
    
        @functools.lru_cache(maxsize = None)
        def go(sm):
            if sm == target:
                return 1
            if sm > target:
                return 0
            res = 0
            for num in nums:
                res += go(sm + num)
            return res
        
        return go(0)
        
