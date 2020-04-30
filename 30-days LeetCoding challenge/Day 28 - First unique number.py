class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums
        self.f = {}
        self.unique_idx = 0
        for e in nums:
            self.f[e] = self.f.get(e, 0) + 1

    def showFirstUnique(self) -> int:
        while self.unique_idx < len(self.q) and self.f.get(self.q[self.unique_idx], 0) != 1:
            self.unique_idx += 1
        if len(self.q) == 0 or self.unique_idx >= len(self.q):
            return -1
        return self.q[self.unique_idx]

    def add(self, value: int) -> None:
        self.q.append(value)
        self.f[value] = self.f.get(value, 0) + 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
