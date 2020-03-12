class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int alph[26] = {0};
        for (auto c : chars) {
            alph[c - 'a']++;
        }
        int res = 0;
        for (auto word : words) {
            int f[30] = {0};
            bool good = true;
            for (auto c : word) {
                f[c - 'a']++;
                good &= f[c - 'a'] <= alph[c - 'a'];
            }
            if (good) {
                res += word.size();
            }
        }
        return res;
    }
};
