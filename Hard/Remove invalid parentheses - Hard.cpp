class Solution {
public:
    
    set<string> sol;
    string s;
    int mx;
    
    void gen(int i, string buf, int op) {
        if (i == s.size() && op == 0) {
            if (buf.size() == mx)
                sol.insert(buf);
            if (buf.size() > mx) {
                mx = buf.size();
                sol.clear();
                sol.insert(buf);
            }
            return;
        }
        if (op < 0 || i == s.size()) return;
        gen(i + 1, buf, op);
        gen(i + 1, buf + s[i], op + ((s[i] == '(') ? 1 : (s[i] == ')') ? -1 : 0));
    }
    
    vector<string> removeInvalidParentheses(string s) {
        this->s = s;
        gen(0, "", 0);
        vector<string> ret;
        for (auto p : sol) ret.push_back(p);
        return ret;
    }
};
