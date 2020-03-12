class Solution {
public:
    bool isPalindrome(int x) {
        stringstream ss;
        ss << x;
        string s = ss.str();
        for (int i = 0; i < s.size() / 2; ++i) {
            int j = s.size() - 1 - i;
            if (s[i] != s[j]) {
                return false;
            }
        }
        return true;
    }
};
