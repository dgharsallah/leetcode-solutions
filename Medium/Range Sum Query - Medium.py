class NumArray:

    def __init__(self, nums: List[int]):
        self.BIT = [0] * (len(nums) + 1)
        self.nums = []
        sum = 0
        for i in range(len(nums)):
            self.nums.append(nums[i])
            self.build(i, nums[i])

    def build(self, i: int, val:int) -> None:
        idx = i + 1
        while idx < len(self.BIT):
            self.BIT[idx] += val
            idx += idx & -idx

    def update(self, i: int, val: int) -> None:
        idx = i + 1
        old = self.nums[i]
        self.nums[i] = val
        while idx < len(self.BIT):
            self.BIT[idx] += val - old
            idx += idx & -idx
    
    def get(self, i: int) -> int:
        sum = 0
        idx = i + 1
        while idx > 0:
            sum += self.BIT[idx]
            idx -= idx & -idx
        return sum

    def sumRange(self, i: int, j: int) -> int:
        return self.get(j) - self.get(i - 1)           
        
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
