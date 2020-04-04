class Solution:
    def isHappy(self, n: int) -> bool:
        states = set()
        num = n
        s = ""
        while True:
            if s in states:
                return False
            # print('s', s, ' num', num)
            states.add(s)
            s = str(num)
            sum = 0
            for c in s:
                d = (ord(c) - ord('0'))
                sum += d * d
            # print('sum ', sum)
            num = sum
            if num == 1:
                return True
