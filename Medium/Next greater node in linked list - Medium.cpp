/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> res(1e4);
        stack<pair<int,int>> s;
        int idx = 0;
        for (; head != NULL; head = head->next) {
            while(!s.empty() && s.top().first < head->val) {
                res[s.top().second] = head->val;
                s.pop();
            }
            s.push({head->val, idx++});
        }
        res.resize(idx);
        return res;
    }
};
