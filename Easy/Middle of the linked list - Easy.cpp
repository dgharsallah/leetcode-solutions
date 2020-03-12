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
    ListNode* middleNode(ListNode* head) {
        ListNode *it = head;
        int length = 0;
        while(it != NULL) {
            it = it->next;
            length++;
        }        
        int i = 0;
        it = head;
        while(it != NULL) {
            if (i >= length / 2) {
                return head;
            }
            i++;
            head = head->next;
        }
        return head;
    }
};
