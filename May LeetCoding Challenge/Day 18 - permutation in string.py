class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_window = Counter(s1)
        window = dict()
        i, j = 0, 0
        positions = []
        while j < len(s2):
            window[s2[j]] = window.get(s2[j], 0) + 1
            if j >= len(s1) - 1:
                if window == target_window:
                    return True
                window[s2[i]] = window.get(s2[i], 0) - 1
                if window[s2[i]] == 0:
                    window.pop(s2[i])
                i += 1
            j += 1
        return False
