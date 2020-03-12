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
    int getDecimalValue(ListNode* head) {
        string s = "";
        while(head != NULL) {
            s += char(head->val + '0');
            head = head->next;
        }
        int res = 0;
        reverse(s.begin(), s.end());
        for (int i = 0; i < s.size(); ++i) {
            res += (1 << i) * (s[i] - '0');
        }
        return res;
    }
};
