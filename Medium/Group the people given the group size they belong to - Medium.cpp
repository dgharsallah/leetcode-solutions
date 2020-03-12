class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        map<int, vector<int>> g;
        set<int> sizes;
        for (int i = 0; i < groupSizes.size(); ++i) {
            g[groupSizes[i]].push_back(i);
            sizes.insert(groupSizes[i]);
        }
        vector<vector<int> > ans;
        for (auto key : sizes) {
            vector<int> v;
            for (auto e : g[key]) {
                v.push_back(e);
                if (v.size() == key) {
                    ans.push_back(v);
                    v.clear();
                }
            }
        }
        return ans;
    }
};
