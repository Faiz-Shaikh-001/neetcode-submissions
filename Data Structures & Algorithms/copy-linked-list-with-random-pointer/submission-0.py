"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hashTable = {}

        while curr:
            newNode = Node(curr.val)
            hashTable[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            hashTable[curr].next = hashTable.get(curr.next, None)
            hashTable[curr].random = hashTable.get(curr.random, None)
            curr = curr.next
        
        return hashTable.get(head, None)