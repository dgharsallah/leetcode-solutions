class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -1e15
        temp = 0
        mx = -1e15
        neg = True
        for e in nums:
            neg &= e < 0
            mx = max(e, mx)
            temp += e
            if temp < 0:
                temp = 0
            if temp > maxSum:
                maxSum = max(temp, maxSum)
        return mx if neg else maxSum
