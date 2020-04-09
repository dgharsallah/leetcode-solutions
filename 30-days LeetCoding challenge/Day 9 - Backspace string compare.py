class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = []
        for c in S:
            if c == '#' and len(a) > 0:
                a.pop()
            elif c != '#':
                a.append(c)
        b = []
        for c in T:
            if c == '#' and len(b) > 0:
                b.pop()
            elif c != '#':
                b.append(c)
        return a == b
