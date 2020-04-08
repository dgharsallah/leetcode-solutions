# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        cnt = 0
        while slow != None and fast != None and fast.next != None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        return slow
            
