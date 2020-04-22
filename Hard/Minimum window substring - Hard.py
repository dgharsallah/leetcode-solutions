class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        dict_t = Counter(t)
        l, r = 0, 0
        ans = 1e9, 0, 0
        window = {}
        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            is_window_valid = True
            for k in dict_t:
                is_window_valid &= window.get(k, 0) >= dict_t[k]
            # compress  while the window has what we need
            while l < r:
                # current window not valid
                if not is_window_valid:
                    break
                # we don't have extra needed character to remove it
                if s[l] in dict_t and window.get(s[l], 0) - dict_t[s[l]] <= 0:
                    break
                # remove character
                if s[l] in window:
                    window[s[l]] -= 1
                l += 1
            # maximize answer
            if r - l + 1 < ans[0] and is_window_valid:
                ans = (r - l + 1, l, r)
            # expand slowly
            r += 1
        return '' if ans[0] == 1e9 else s[ans[1]: ans[2] + 1]
