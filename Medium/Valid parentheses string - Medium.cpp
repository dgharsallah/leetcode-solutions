class Solution {
public:
    bool checkValidString(string s) {
        stack<int> op, stars;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                op.push(i);
            } else if (s[i] == ')') {
                if (!op.empty()) op.pop();
                else if (!stars.empty()) stars.pop();
                else return false; // treat case of a closing bracket with no open bracket before it
            } else {
                stars.push(i);
            }
        }
        while(!op.empty() && !stars.empty()) {
            // return false when asterik comes before opening bracket
            if (op.top() >= stars.top())
                return false;
            op.pop();
            stars.pop();
        }
        return op.size() == 0;
    }
};
