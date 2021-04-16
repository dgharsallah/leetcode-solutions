class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        pads = ["", "" , "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        buf = []
        
        def generate(i):
            if i == len(digits):
                res.append("".join(buf))
                return
            # print(int(ord(digits[i]) - ord('0')))
            for num in pads[int(ord(digits[i]) - ord('0'))]:
                buf.append(num)
                generate(i + 1)
                buf.pop()
        
        generate(0)
        return res
