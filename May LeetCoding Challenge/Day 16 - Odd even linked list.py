# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        ans = []
        for i in range(0, len(a), 2):
            ans.append(a[i])
        for i in range(1, len(a), 2):
            ans.append(a[i])
        ll = ListNode()
        for e in reversed(ans):
            temp = ListNode()
            ll.val = e
            temp.next = ll
            ll = temp
        return ll.next
