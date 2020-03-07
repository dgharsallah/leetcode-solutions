class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        vector<vector<int>> in(N, vector<int>()), out(N, vector<int>());
        for (auto pr : trust) {
            int u = pr[0] - 1, v = pr[1] - 1;
            out[u].push_back(v);
            in[v].push_back(u);
        }
        for (int i = 0; i < N; ++i) {
            if (in[i].size() == N - 1 && out[i].size() == 0) {
                return i + 1;
            }
        }
        return -1;
    }
};
