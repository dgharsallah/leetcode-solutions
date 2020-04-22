# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def merged(l1, l2):
            if l1 is None and l2 is None:
                return None
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if l1.val < l2.val:
                ret = ListNode(l1.val)
                l1 = l1.next
                ret.next = merged(l1, l2)
                return ret
            ret = ListNode(l2.val)
            l2 = l2.next
            ret.next = merged(l1, l2)
            return ret
        
        return merged(l1, l2)
