class Solution {
public:
    
    vector<int> c;
    int targ;
    set<vector<int> > solutions;
    
    void go(int i, vector<int> buff, int sum) {
        if (i == c.size() || sum > targ) {
            if (sum == targ)
                solutions.insert(buff);
            return;
        }
        go(i + 1, buff, sum);
        sum += c[i];
        buff.push_back(c[i]);
        go(i, buff, sum);
        go(i + 1, buff, sum);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int> > ans;
        targ = target;
        c = candidates;
        go(0, vector<int>(), 0);
        for (auto sol : solutions) {
            vector<int> tmp;
            for (auto e : sol)  {
                tmp.push_back(e);
            }
            ans.push_back(tmp);
        }
        return ans;       
    }
};
