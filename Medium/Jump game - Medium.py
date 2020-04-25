class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        while cur < len(nums):
            nxt = cur
            reach = 0
            if cur == len(nums) - 1:
                return True
            for jump in range(nums[cur]):
                temp_nxt = cur + jump + 1
                if temp_nxt < len(nums):
                    temp_reach = temp_nxt + nums[temp_nxt]
                    if temp_reach > reach:
                        nxt = temp_nxt
                        reach = temp_reach
            if nxt == cur:
                return False
            cur = nxt
        return False
