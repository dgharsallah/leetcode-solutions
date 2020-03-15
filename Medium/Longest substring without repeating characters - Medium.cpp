class Solution {
public:

    int lengthOfLongestSubstring(string s) {
        int ans = 0, l = 0, r = 0;
        set<int> st;
        while(r < s.size() && l < s.size()) {
            if (st.find(s[r]) == st.end()) {
                st.insert(s[r]);
                r++;
            } else {
                st.erase(s[l]);
                l++;
            }
            ans = max(ans, (int)st.size());
        }
        return ans;
    }
};
