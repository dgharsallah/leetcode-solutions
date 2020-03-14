class Solution {
public:
    
    vector<string> ans;
    int l;
    
    void get(int i, int op, string buff) {
        // cout << l << endl;
        if (i >= 2*l) {
            if (op == 0) ans.push_back(buff);
            return;
        }
        if (op < 0 || op > l) return;
        get(i + 1, op + 1, buff + "(");
        get(i + 1, op - 1, buff + ")");
    }
    
    vector<string> generateParenthesis(int n) {
        l = n;
        get(0, 0, "");
        return ans;
    }
};
