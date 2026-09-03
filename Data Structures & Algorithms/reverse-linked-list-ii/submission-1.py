# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Tracks the node before the start of reversed section
        before_left = None

        i = 0
        curr = head
        while i < left - 1:
            before_left = curr
            curr = curr.next
            i += 1
        
        prev, next = None, None
        tail = curr
        while curr and i < right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        
        tail.next = next
        if before_left:
            before_left.next = prev
        return head if before_left else prev
