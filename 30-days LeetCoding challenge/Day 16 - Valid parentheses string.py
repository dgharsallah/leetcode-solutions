class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        asteriks = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                st.append(i)
            elif c == ')':
                if len(st) > 0:
                    st.pop()
                elif len(asteriks) > 0:
                    asteriks.pop()
                else:
                    return False
            else:
                asteriks.append(i)
        while len(asteriks) > 0 and len(st) > 0 and asteriks[-1] > st[-1]:
            asteriks.pop()
            st.pop()
        return len(st) == 0
