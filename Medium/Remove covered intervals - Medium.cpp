class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int> b) {
            if (a[0] == b[0]) {
                return b[1] > a[1];
            }
            return a[0] < b[0];
        });
        for (int i = 1; i < intervals.size(); ++i) {
            int l1 = intervals[i][0], r1 = intervals[i][1];
            int l0 = intervals[i - 1][0], r0 = intervals[i - 1][1];
            if (l0 <= l1 && r1 <= r0) {
                intervals.erase(intervals.begin() + i);
                --i;
            }
        }
        return intervals.size();
    }
};
