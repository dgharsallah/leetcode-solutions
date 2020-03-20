class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        set<pair<int, int> > s;
        vector<int> ans(T.size(), 0);
        vector<int> last(101, 0);
        for (int i = T.size() - 1; i >= 0; --i) {
            last[T[i]] = i;
            int found = 1e9, at;
            for (int temp = T[i] + 1; temp <= 100; temp++) {
                if (last[temp] > 0 && last[temp] < found) {
                    found = last[temp];  
                    // at = tmp;
                }
            }
            if (found != 1e9) {
                ans[i] = found - i;
            }
        }
        return ans;
    }
};
