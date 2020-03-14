class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> f;
        for (auto e : nums) f[e]++;
        priority_queue<pair<int, int> > pq;
        for (auto p : f) pq.push({p.second, p.first});
        vector<int> ans;
        while(k--) {
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
