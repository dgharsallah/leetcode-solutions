class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_window = Counter(p)
        window = dict()
        i, j = 0, 0
        positions = []
        while j < len(s):
            window[s[j]] = window.get(s[j], 0) + 1
            if j >= len(p) - 1:
                if window == target_window:
                    positions.append(i)
                window[s[i]] = window.get(s[i], 0) - 1
                if window[s[i]] == 0:
                    window.pop(s[i])
                i += 1
            j += 1
        return positions
