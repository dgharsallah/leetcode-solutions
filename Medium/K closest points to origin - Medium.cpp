class Solution {
public:
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<pair<double, pair<int, int> > > p;
        for (auto pt : points) {
            int x = pt[0], y = pt[1];
            double dist = sqrt(x * x + y * y);
            p.push_back({dist, {x, y}});
        }
        sort(p.begin(), p.end());
        vector<vector<int>> ans(K, vector<int>());
        for (int i = 0; i < K; ++i) {
            ans[i].push_back(p[i].second.first);
            ans[i].push_back(p[i].second.second);
        }
        return ans;
    }
};
