class Solution {
public:
    string frequencySort(string s) {
        map<char, int> m;
        for (char c : s) {
            m[c]++;
        }
        string ans = "";
        priority_queue<pair<int, char>> pq;
        for (auto p : m) {
            pq.push({p.second, p.first});
        }
        while(!pq.empty()) {
            pair<int, char> p = pq.top();
            pq.pop();
            ans += string(p.first, p.second);
        }
        return ans;
    }
};
