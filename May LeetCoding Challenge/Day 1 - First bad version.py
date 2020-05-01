# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r, ans = 1, n, 0
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
