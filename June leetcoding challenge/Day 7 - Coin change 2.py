class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1
        
        @lru_cache(maxsize=None)
        def calc(rem, coinIdx):
            if rem <= 0 or coinIdx >= len(coins):
                return (rem == 0) * (coinIdx < len(coins))
            return calc(rem, coinIdx + 1) + calc(rem - coins[coinIdx], coinIdx)
        
        return calc(amount, 0)
