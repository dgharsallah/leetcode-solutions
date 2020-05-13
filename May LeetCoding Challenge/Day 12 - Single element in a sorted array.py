class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            is_even = (r - mid) % 2 == 0
            if mid == len(nums) - 1 or mid == 0:
                return nums[mid]
            if nums[mid + 1] == nums[mid]:
                if is_even:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if is_even:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]
