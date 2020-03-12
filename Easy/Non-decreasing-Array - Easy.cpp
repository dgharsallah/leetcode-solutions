class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        vector<int> l(n + 2, 1), r(n + 2, 1), v(n + 2, 0);
        v[0] = -1e6;
        v[n + 1] = 1e6;
        for (int i = 1; i <= n; ++i) {
            v[i] = nums[i - 1];
            // start here
            l[i] = l[i - 1] & (v[i - 1] <= v[i]);
        }
        for (int i = n; i >= 1; --i) {
            r[i] = r[i + 1] && (v[i] <= v[i + 1]);
        }
        for (int i = 1; i <= n; ++i) {
            if (l[i - 1] && r[i + 1] && v[i - 1] <= v[i + 1]) {
                return true;
            }
        }
        return false;
    }
};
