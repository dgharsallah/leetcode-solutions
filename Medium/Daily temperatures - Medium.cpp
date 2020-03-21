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
    /* 
    // A faster solution using stack
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        stack<int> s;
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            while(!s.empty() && T[s.top()] < T[i]) {
                res[s.top()] = i - s.top();
                s.pop();
            }
            s.push(i);
        }
        return res;
    }
    */
};
