# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        tortoise = head
        while hare != None and tortoise != None:
            if hare.next != None and hare.next.next != None:
                hare = hare.next.next
            else:
                break
            if tortoise.next != None:
                tortoise = tortoise.next
            else:
                break
            if hare.val == tortoise.val:
                return True
        return False
