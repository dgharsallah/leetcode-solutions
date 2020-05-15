class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        a = [0]
        a.extend(A + A)
        
        def kadane():
            max_sum, max_so_far, max_start = -1e9, 0, 0
            for e in A:
                max_so_far = max_so_far + e
                if max_so_far > max_sum:
                    max_sum = max_so_far
                if max_so_far < 0:
                    max_so_far = 0
            return max_sum
        
        ans = kadane()
        tot = 0
        all_neg = True
        max_element = -1e9
        for i in range(len(A)):
            all_neg &= A[i] < 0
            max_element = max(max_element, A[i])
            tot += A[i]
            A[i] *= -1
        if all_neg:
            return max_element
        return max(ans, tot + kadane())
