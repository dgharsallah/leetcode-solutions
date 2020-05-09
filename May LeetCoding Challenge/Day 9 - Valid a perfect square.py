class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r, mid = 1, 1e9, 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
