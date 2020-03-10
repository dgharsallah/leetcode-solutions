class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = 0, p2 = 0, p = 0;
        // nums.resize(m);
        vector<int> ans(n + m, 0);
        while(p1 < m && p2 < n) {
            if (nums1[p1] > nums2[p2]) {
                ans[p] = nums2[p2];
                p2++;
            } else {
                ans[p] = nums1[p1];
                ++p1;
            }
            ++p;
        }
        while(p1 < m) {
            ans[p] = nums1[p1];
            ++p;
            ++p1;
        }
        while(p2 < n) {
            ans[p] = nums2[p2];
            ++p;
            ++p2;
        }
        nums1 = ans;
    }
};
