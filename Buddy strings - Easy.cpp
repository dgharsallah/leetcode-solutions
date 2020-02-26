class Solution {
public:
    bool buddyStrings(string A, string B) {
        if (A.size() != B.size()) {
            return false;
        }
        bool dup = false;
        string buf1 = "", buf2 = "", c = A;
        for (int i = 0; i < A.size(); ++i) {
            if (A[i] != B[i]) {
                buf1 += A[i];
                buf2 += B[i];
            }
        }
        sort(c.begin(), c.end());
        for (int i = 1; i < c.size(); ++i) {
            dup |= c[i] == c[i - 1];
        }
        if ((buf1.size() != 2 || buf2.size() != 2) && !dup) {
            return false;
        }
        return buf1.front() == buf2.back() && buf1.back() == buf2.front();
    }
};
