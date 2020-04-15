class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if i > 0:
                ans.append(ans[-1] * nums[i - 1])
            else:
                ans.append(1)
        r = 1
        for i in reversed(range(len(nums))):
            ans[i] *= r
            r *= nums[i]
        return ans
