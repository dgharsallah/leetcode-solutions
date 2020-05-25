class Solution:
    def frequencySort(self, s: str) -> str:
        f = Counter(s)
        l = []
        for c in f:
            l.append((f[c], c))
        heapq.heapify(l)
        ans = ''
        while len(l):
            h = heapq.heappop(l)
            ans += h[0] * h[1]
        return ans[::-1]
