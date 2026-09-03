# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr_ahead, curr = dummy, dummy
        
        i = 0
        while curr_ahead and i <= n:
            curr_ahead = curr_ahead.next
            i += 1
        
        while curr_ahead:
            curr_ahead = curr_ahead.next
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next