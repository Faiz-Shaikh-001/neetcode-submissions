# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        curr = second
        prev, next = None, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first_next, second_next = None, None
        while prev:
            first_next = head.next
            second_next = prev.next
            head.next = prev
            prev.next = first_next
            head = prev.next
            prev = second_next