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
    
    void reverseLL(ListNode *head, queue<int>& q) {
        if (head == NULL) {
            return;
        }
        q.push(head->val);
        reverseLL(head->next, q);
        head->val = q.front();
        q.pop();
    }
    
    ListNode* reverseList(ListNode* head) {
        queue<int> q;
        reverseLL(head, q);
        return head;
        // --Iterative solution below--
        // ListNode* resHead = head;
        // vector<int> v;
        // while(resHead != NULL) {
        //     v.push_back(resHead->val);
        //     resHead = resHead->next;
        // }
        // resHead = head;
        // reverse(v.begin(), v.end());
        // for (auto e : v) {
        //     resHead->val = e;
        //     resHead = resHead->next;
        // }
        // return head;
    }
};
