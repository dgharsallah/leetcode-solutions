class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        map<int, int> inv;
        inv['('] = ')';
        inv['['] = ']';
        inv['{'] = '}';
        for (auto c : s) {
            if ((c == '(' || c == '{') || c == '[') {
                st.push(c);
            } else if (!st.empty() && inv[st.top()] == c) {
                st.pop();
            } else
                return false;
        } 
        return st.empty();
    }
};
