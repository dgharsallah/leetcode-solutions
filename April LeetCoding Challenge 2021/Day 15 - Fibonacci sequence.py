class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, 100):
            f.append(f[-1] + f[-2])
        return f[n]
        
