class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            s = set()
            for j in range(i + 1, n):
                rem = -nums[i]-nums[j]
                if rem in s:
                    ans.add((nums[i], nums[j], rem))
                else:
                    s.add(nums[j])
        return list(ans)
