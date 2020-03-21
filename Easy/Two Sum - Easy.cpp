class Solution {
public:
    // brute force solution O(n^2)
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i == j) {
                    continue;
                }
                if (nums[i] + nums[j] == target) {
                    v.push_back(i);
                    v.push_back(j);
                    break;
                }
            }
            if (!v.empty()) {
                break;
            }
        }
        return v;
    }
    
    // optimized solution using HashTable O(n)
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.find(nums[i]) == m.end()) {
                m[target - nums[i]] = i;
            } else {
                v = {i, m[nums[i]]};
                break;
            }
        }
        return v;
    }
};
