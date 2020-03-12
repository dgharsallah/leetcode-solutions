class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        if (strs.empty()) {
            return "";
        }
        for (int i = 0; i < strs[0].size(); ++i) {
            char c = strs[0][i];
            bool good = true;
            for (int j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].size()) {
                    good = false;
                    break;
                }
                if (c != strs[j][i]) {
                    good = false;
                    break;
                }
            }
            if (good) {
                res += c;
            } else {
                break;
            }
        }
        return res;
    }
};
