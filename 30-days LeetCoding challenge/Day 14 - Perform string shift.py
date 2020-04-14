class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        totalShift = 0
        for sh in shift:
            totalShift += sh[1] if sh[0] == 1 else -sh[1]
        l = len(s)
        totalShift = (l - totalShift) % l
        print(totalShift)
        s += s
        return s[totalShift:totalShift + l]
