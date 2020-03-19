class Solution {
public:
    
    vector<vector<int> > sol;
    vector<int> tmp;
    int N;
    
    void gen(int i, int rem) {
        if (rem < 0 || i > N) return;
        if (i == N) {
            if (rem == 0)
                sol.push_back(tmp);
            return;
        }
        gen(i + 1, rem);
        tmp.push_back(i + 1);
        gen(i + 1, rem - 1);
        tmp.pop_back();
    }
    
    vector<vector<int>> combine(int n, int k) {
        N = n;
        gen(0, k);
        return sol;
    }
};
