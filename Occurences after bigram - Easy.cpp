class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        stringstream ss(text);
        vector<string> v, ans;
        string s;
        while(ss >> s) {
            v.push_back(s);
        }
        for (int i = 0; i < v.size() - 2; ++i) {
            if (v[i] == first && v[i + 1] == second) {
                ans.push_back(v[i + 2]);
            }
        }
        return ans;
    }
};
