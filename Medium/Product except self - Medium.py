class Solution:
    # solution 1: 
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
      # solution 2
      def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [1] * len(nums)
        pref = [1] * len(nums)
        for i in range(len(nums)):
            pref[i] = nums[i]
            if i == 0:
                continue
            pref[i] *= pref[i - 1]
        for i in reversed(range(len(nums))):
            suf[i] = nums[i]
            if i == len(nums) - 1:
                continue
            suf[i] *= suf[i + 1]
        ans = []
        for i in range(len(nums)):
            l = pref[i - 1] if i > 0 else 1
            r = suf[i + 1] if i < len(nums) - 1 else 1
            ans.append(l * r)
        return ans
