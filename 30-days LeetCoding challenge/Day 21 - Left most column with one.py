# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        n, m = binaryMatrix.dimensions()
        
        def has_one(col):
            for row in range(n):
                if binaryMatrix.get(row, col):
                    return True
            return False
        
        l, r, mid, ans = 0, m - 1, 0, -1
        while l <= r:
            mid = l + (r - l) // 2
            if has_one(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
