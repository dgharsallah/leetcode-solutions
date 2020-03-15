class Solution {
public:
    
    string longestPalindrome(string s) {
        if (s == "") return "";
        int n = s.size(), maxLen = 1, L = 0, R;
        for (int i = 1; i < n; ++i) {
            int l = i - 1, r = i;
            while(l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    L = l;
                    R = r;
                }
                --l, r++;   
            }
            l = i - 1, r = i + 1;
            while(l >= 0 && r < n && s[l] == s[r]) { 
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    L = l;
                    R = r;
                }
                --l, r++;  
            }
        }
        return s.substr(L, maxLen);
    }
};
