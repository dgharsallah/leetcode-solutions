class Solution {
public:
    
    int dfs = 1;
    vector<int> idx, low;
    vector<vector<int>> g, bridges;
    int root, child = 0;

    void DFS(int u, int p) {
        low[u] = idx[u] = dfs++;
        for (int i = 0; i < g[u].size(); ++i)
            if (idx[g[u][i]] == 0) {
                if (root == u)
                    ++child;
                DFS(g[u][i], u);
                low[u] = min(low[u], low[g[u][i]]);
                int v = g[u][i];
                if (low[v] > idx[u])
                    bridges.push_back({min(u, v), max(u, v)});
            } else if (p != g[u][i])
                low[u] = min(low[u], idx[g[u][i]]);
    }
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        g.resize(n);
        idx.resize(n);
        low.resize(n);
        for (int i = 0; i < connections.size(); ++i) {
            g[connections[i][0]].push_back(connections[i][1]);
            g[connections[i][1]].push_back(connections[i][0]);
        }
        root = 0;
        DFS(root, -1);
        return bridges;
    }
};
