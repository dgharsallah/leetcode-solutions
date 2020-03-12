class Solution {
public:
    
    vector<int> a;
    vector<vector<int> > ans;
    
    void getCombinations(int i, vector<int> tmp) {
       if (i == a.size()) {
            ans.push_back(tmp);
            return;
       }
        getCombinations(i + 1, tmp);
        tmp.push_back(a[i]);
        getCombinations(i + 1, tmp);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        a = nums;
        getCombinations(0, vector<int>());
        return ans;
    }
};
