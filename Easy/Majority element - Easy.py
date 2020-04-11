class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        maxF = 0
        mostF = 0
        for num in nums:
            if f.get(num) == None:
                f[num] = 1
            else:
                f[num] += 1
            if f[num] > maxF:
                maxF = f[num]
                mostF = num
        return mostF
