class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @lru_cache(maxsize=None)
        def play(l, r, turn):
            if r < l:
                return 0
            a = play(l + 1, r, -turn) + nums[l] * turn
            b = play(l, r - 1, -turn) + nums[r] * turn
            return turn * max(a * turn, b * turn)
    
        return play(0, len(nums) - 1, 1)  >= 0
