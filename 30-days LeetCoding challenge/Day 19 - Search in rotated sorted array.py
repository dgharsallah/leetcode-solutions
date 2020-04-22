class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        pivot = 0
        while l <= r:
            mid = l + (r - l) // 2
            start = nums[l]
            end = nums[r]
            cur = nums[mid]
            if cur == target:
                return mid
            # second sorted part
            if cur < start:
                if cur <= target and target <= end:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # first sorted part
                if start <= target and target <= cur:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
