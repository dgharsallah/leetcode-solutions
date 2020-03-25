class Solution {
public:
    
    string pads[10] = {"", "" , "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> sol;
    string digits;
    
    void gen(int i, string buf) {
      if (i == digits.size()) {
        sol.push_back(buf);
        return;
      }
      for (auto c : pads[digits[i] - '0']) {
        gen(i + 1, buf + c);
      }
    }
    
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        this->digits = digits;
        gen(0, "");
        return sol;
    }
};
